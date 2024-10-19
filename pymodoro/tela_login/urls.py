from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.tela_login, name='tela_login'),
]
