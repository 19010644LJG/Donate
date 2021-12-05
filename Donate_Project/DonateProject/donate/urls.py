from django.urls import path
from . import views

urlpatterns = [
    path('donate/', views.donate, name='donate'),
    path('donate_pay/', views.donate_pay, name='donate_pay'),
    path('donate_admin/', views.donate_admin, name='donate_admin'),
    path('donate_accept/<int:id>', views.donate_accept, name='donate_accept'),
    path('donate_confirm/', views.donate_confirm, name='donate_confirm')
]
