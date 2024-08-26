from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import TicketPurchaseForm
import stripe
from events.models import Event
from .models import Payment

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def purchase_ticket(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = TicketPurchaseForm(request.POST)
        if form.is_valid():
            try:
                # Calculate the total amount in cents
                total_amount = int(event.ticket_price * form.cleaned_data['quantity'] * 100)  # Stripe handles payments in cents

                # Create a PaymentIntent with manual confirmation
                intent = stripe.PaymentIntent.create(
                    amount=total_amount,
                    currency='usd',
                    payment_method=request.POST.get('payment_method_id'),
                    confirmation_method='manual',
                    confirm=True,  # Confirm the payment
                    return_url=request.build_absolute_uri(reverse('profile')),  # Redirect to the profile after purchase
                )

                print("PaymentIntent created successfully: ", intent)  # Debugging statement

                # Save the ticket after payment is successful
                ticket = form.save(commit=False)
                ticket.event = event
                ticket.user = request.user
                ticket.stripe_payment_intent_id = intent['id']
                ticket.save()  # This will trigger the QR code generation

                # Check if the payment was successfully confirmed
                if intent['status'] == 'succeeded':
                    payment_status = 'Completed'
                elif intent['status'] in ['requires_action', 'requires_confirmation']:
                    payment_status = 'Pending'
                else:
                    payment_status = 'Failed'

                # Retrieve the latest charge if available
                receipt_url = None
                if 'latest_charge' in intent and intent['latest_charge']:
                    charge = stripe.Charge.retrieve(intent['latest_charge'])
                    receipt_url = charge.get('receipt_url')

                # Save payment details
                payment = Payment(
                    user=request.user,
                    ticket=ticket,
                    stripe_payment_intent_id=intent['id'],
                    amount=total_amount / 100,  # Convert cents to dollars
                    status=payment_status,  # Set based on Stripe's payment status
                    receipt_url=receipt_url
                )
                payment.save()

                # Provide appropriate user feedback based on payment status
                if payment_status == 'Completed':
                    messages.success(request, 'Ticket purchased successfully!')
                elif payment_status == 'Pending':
                    messages.warning(request, 'Your payment is pending confirmation. Please check your email for further instructions.')
                else:
                    messages.error(request, 'Your payment could not be completed. Please try again.')

                return redirect('profile')  # Redirect to the profile page after a successful purchase

            except stripe.error.CardError as e:
                # The card has been declined
                messages.error(request, f"Your card was declined: {e.error.message}")
                print(f"CardError: {e.error.message}")  # Debugging statement
            except stripe.error.StripeError as e:
                # Some other Stripe error occurred
                messages.error(request, "Something went wrong with your payment. Please try again.")
                print(f"StripeError: {e}")  # Debugging statement
            except Exception as e:
                # Catch-all for any other errors
                messages.error(request, "An unexpected error occurred. Please try again.")
                print(f"Unexpected error: {e}")  # Debugging statement
        else:
            print("Form is invalid: ", form.errors)  # Print form errors to the console/log for debugging
            messages.error(request, "There was a problem with your form submission.")
    else:
        form = TicketPurchaseForm()

    return render(request, 'tickets/purchase_ticket.html', {
        'form': form,
        'event': event,
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY,
    })

@login_required
def payment_history(request):
    payments = Payment.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'payments/payment_history.html', {'payments': payments})
