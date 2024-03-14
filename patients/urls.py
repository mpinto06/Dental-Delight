from django.urls import path, include
from . import views

app_name = "patients"

urlpatterns = [
    path("", views.patients_list, name="list"),
    path("add/", views.patients_add, name="add"),
    path('<int:pk>/', views.patients_details, name='details'),
    path('<int:pk>/edit/', views.patients_edit, name='edit'),
    path('<int:pk>/delete/', views.patients_delete, name='delete'),
]