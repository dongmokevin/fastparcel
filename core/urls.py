from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home),
    path('customer/', views.customer_page),
    path('courier/', views.courier_page),
    path('sign-up/', views.sign_up),
]
