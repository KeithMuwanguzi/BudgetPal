from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login),
    path('register/',views.register),
    path('users/',views.getUsers),
    path('test_token/',views.testToken),
]