from django.urls import path
from . import views

app_name = "appointments"

urlpatterns = [
    path("", views.appointments_list, name="list"),
    path("<int:fk>/schedule", views.appointments_add, name="add"),
    path('<int:pk>/', views.appointments_details, name='details'),
    path('<int:pk>/edit/', views.appointments_edit, name='edit'),
    path('<int:pk>/delete/', views.appointments_delete, name='delete'),
]