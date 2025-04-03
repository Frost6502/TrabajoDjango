from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("tasks.urls")),
    path("api/", include("tasks.api_urls")),
    path("accounts/", include("django.contrib.auth.urls")), 
]
 