from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from event_management import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Include core.urls at the root
    path('users/', include('users.urls')),
    path('events/', include('events.urls')),
    path('tickets/', include('tickets.urls')),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)