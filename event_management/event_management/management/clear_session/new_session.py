from django.contrib.sessions.models import Session

class ClearSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
        self.clear_sessions()

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def clear_sessions(self):
        Session.objects.all().delete()
