from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('edition/<int:curso>/', views.edition, name='edition'),
    path('edition/<int:curso>/<int:id>/', views.presentation, name='presentation'),
]
