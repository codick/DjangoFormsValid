from django.urls import path
from valid_app import views

urlpatterns = [
    path('registration/', views.index, name='index'),
    path('sign/', views.sign, name='sign'),
]