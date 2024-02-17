from django.urls import path, include
from .views import home


urlpatterns = [
    path("", include('allauth.urls')),
    path("home/", home, name="home")
]