from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView, DetailView, ListView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.urls import reverse
from . import forms
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404

from .models import Address

#user email validator libraries
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.core.mail import send_mail
from .forms import CustomSignUpForm
from .forms import HomeAddress
from .forms import GenderSelect
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes





# Create your views here.

class LandingPageView(TemplateView):
    template_name = 'landing/Global_Aid_Network_Latvia_Landing.html'

class AboutUsView(TemplateView):
    template_name='landing/About_Us.html'

class OurWorkView(TemplateView):
    template_name = 'landing/Our_Work.html'

class GetInvolvedView(TemplateView):
    template_name='landing/get_involved.html'

class StoriesView(TemplateView):
    template_name = 'landing/stories.html'

class ContactView(TemplateView):
    template_name = 'landing/contact.html'

@login_required
def user_profile(request, username):
        
        user = get_object_or_404(User, username=username)
        address = getattr(user, "address",None)
        gender = getattr(user, "gender", None)

        print("PROFILE USER:", user.username)
        print("ADDRESS FOUND:", address)

        
        return render(request, "landing/user_profile.html", {"profile_user": user, "address":address, "gender": gender})




class SignUp(CreateView):
    form_class = forms.CustomSignUpForm
    success_url = reverse_lazy('login')
    template_name = 'landing/signup.html'


def signup(request):
    if request.method == "POST":
       user_form = CustomSignUpForm(request.POST)
       address_form = HomeAddress(request.POST)
       gender_form = GenderSelect(request.POST)
       if user_form.is_valid() and gender_form.is_valid() and address_form.is_valid():
            user = user_form.save(commit=False)
            user.is_active = False
            user.save() 

            gender = gender_form.save(commit=False)
            gender.user = user 
            gender.save()

            address = address_form.save(commit=False)
            address.user = user
            address.save()

            uid = urlsafe_base64_encode(force_bytes(user.pk))

            token = default_token_generator.make_token(user)
            domain = get_current_site(request).domain
            link = f"http://{domain}/activate/{uid}/{token}/"
            print("✅ Email link:", link) 
            send_mail(
                "Confirm your email",
                f"Click to verify : {link}",
                "no-reply@yourdomain.com",
                [user.email],
            )
            return render(
                request,
                "landing/email_verification_sent.html",
                {"email": user.email}
            )
           
    else:
        user_form = CustomSignUpForm()
        gender_form= GenderSelect()
        address_form = HomeAddress()

    return render(request, "landing/signup.html", {"user_form":user_form, "gender_form":gender_form, "address_form":address_form})
    #


User = get_user_model()

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except Exception:
        user=None

    if user and default_token_generator.check_token(user,token):
        user.is_active=True
        user.save()
        return render(request, "landing/email_verified.html",{"user":user})
    
    return HttpResponse ("Activation link is invalid or expired")

def logout_view(request):
    logout(request)
    print(request.session.keys())
    return redirect('landing:landing_page') 



