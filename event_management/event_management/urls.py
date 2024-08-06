from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Include core.urls at the root
    path('api/', include('users.urls')),
    path('events/', include('events.urls')),
]
