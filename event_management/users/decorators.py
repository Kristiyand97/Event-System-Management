from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages


def email_verified_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('account_login')
        if not request.user.emailaddress_set.filter(verified=True).exists():
            messages.error(request, "Please verify your email address to create an event.")
            return redirect('profile')  # or wherever you want to redirect the user
        return view_func(request, *args, **kwargs)

    return _wrapped_view
