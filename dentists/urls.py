from django.urls import path, include
from . import views

app_name = "dentists"

urlpatterns = [
    path("", views.dentists_list, name="list"),
    path("add/", views.dentist_add, name="add"),
    path('<int:pk>/', views.dentists_details, name='details'),
    path('<int:pk>/edit/', views.dentists_edit, name='edit'),
    path('<int:pk>/delete/', views.dentists_delete, name='delete'),
]