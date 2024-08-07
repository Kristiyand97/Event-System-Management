from django.shortcuts import render

def home(request):
    # Example dynamic content
    context = {
        'title': 'Welcome to Event Management',
        'events': [
            {'name': 'Event 1', 'date': '2024-08-01', 'location': 'New York'},
            {'name': 'Event 2', 'date': '2024-08-15', 'location': 'Los Angeles'},
            {'name': 'Event 3', 'date': '2024-09-10', 'location': 'Chicago'},
        ]
    }
    return render(request, 'core/home.html', context)


def about(request):
    return render(request, 'core/about.html')

def services(request):
    return render(request, 'core/services.html')

def contact(request):
    return render(request, 'core/contact.html')