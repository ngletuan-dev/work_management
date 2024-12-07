from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('checkin/', views.check_in, name='check_in'),
    path('checkout/', views.check_out, name='check_out'),
    path('shifts/', views.shifts, name='shifts'),
]
