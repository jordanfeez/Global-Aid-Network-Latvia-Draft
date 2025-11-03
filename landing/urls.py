from landing import views
from django.urls import path
from django.urls import re_path
from django.contrib.auth import views as auth_views


app_name= 'landing'


urlpatterns  = [
    path('', views.LandingPageView.as_view(), name="landing_page"),
    path("login/",auth_views.LoginView.as_view(template_name='landing/login.html'),name='login'),
    path("logout/",auth_views.LogoutView.as_view(),name='logout'),
   # path("signup/",views.SignUp.as_view(template_name='landing/signup.html'),name='signup'),
    path("signup/", views.signup, name='signup'),
    path('activate/<uidb64>/<token>/',views.activate,name='activate'),
    path('about/', views.AboutUsView.as_view(),name='aboutus'),
    path('ourwork/', views.OurWorkView.as_view(), name='our_work'),
]