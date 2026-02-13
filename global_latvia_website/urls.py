"""
URL configuration for global_latvia_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from landing import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing.urls', namespace='landing')),
    path("signup/", views.SignUp.as_view(), name='signup'),
    path("accounts/", include('django.contrib.auth.urls')),
    path('about/',views.AboutUsView.as_view(),name='aboutus'),
    path('ourwork/',views.OurWorkView.as_view(),name='our_work'),
    path('get_involved/',views.GetInvolvedView.as_view(),name='get_involved'),
    path('stories/', views.StoriesView.as_view(), name= 'stories'),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('profile/<str:username>/',views.user_profile, name='user_profile'),
    path("logout/",views.logout_view,name='logout'),
    path('fundraise/<str:username>/',views.FundraiseView.as_view(), name='fundraise')

]
