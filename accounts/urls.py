from django.urls import path
from . import views
from django.contrib import auth

app_name='accounts'

urlpatterns=[
    path('signup/',views.SignUp.as_view(),name="signup"),
    #path('sign_up',views.SignUp.as_view(),name="signup"),
]