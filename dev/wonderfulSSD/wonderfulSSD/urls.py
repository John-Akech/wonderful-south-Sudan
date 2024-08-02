from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crm.urls', namespace='crm')),  # Include app URLs with namespace
]
