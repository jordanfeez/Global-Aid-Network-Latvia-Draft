from landing import views
from django.urls import path
from django.urls import re_path
from django.contrib.auth import views as auth_views
from landing.views import logout_view


app_name= 'landing'


urlpatterns  = [
    path('', views.LandingPageView.as_view(), name="landing_page"),
    path("login/", auth_views.LoginView.as_view(
        template_name='landing/login.html'
    ), name='login'),
    path("logout/",views.logout_view,name='logout'),
   # path("signup/",views.SignUp.as_view(template_name='landing/signup.html'),name='signup'),
    path("signup/", views.signup, name='signup'),
    path('activate/<uidb64>/<token>/',views.activate,name='activate'),
    path('about/', views.AboutUsView.as_view(),name='aboutus'),
    path('ourwork/', views.OurWorkView.as_view(), name='our_work'),
    path('get_involved/', views.GetInvolvedView.as_view(), name='get_involved'),
    path('stories/', views.StoriesView.as_view(), name='stories'),
    path('contact/',views.ContactView.as_view(), name='contact'),
    path('profile/<str:username>/', views.UserProfileView.as_view(), name='user_profile'),
]