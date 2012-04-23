# -*- coding: utf-8 -*-
# Create your views here.
from django import forms
from django.core import validators
from django.core.mail import send_mail
from django.core.files import File
from django.core.exceptions import ValidationError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.template import RequestContext
from registrations.models import UserProfile
import hashlib, random, datetime

class RegistrationForm(forms.Form):
    username = forms.SlugField(min_length=4, max_length=16)
    email = forms.EmailField(max_length=30)
    password = forms.CharField(min_length=6, max_length=16, widget=forms.PasswordInput)
    password_confirm = forms.CharField(min_length=6, max_length=16, widget=forms.PasswordInput)
    
    def save(self):
        d = self.cleaned_data
        u = User.objects.create_user(username=d['username'],
                                     password=d['password'],
                                     email=d['email'])
        u.set_password(d['password'])
        u.is_active = False
        u.save()
        return u    
    
    def clean_username(self):
        value = self.cleaned_data['username']
        try:
            User.objects.get(username=value)
        except User.DoesNotExist:
            return value
        raise ValidationError(u'Username "%s" has been used.' % value)
    
    def clean(self):
        if cmp(self.cleaned_data.get('password'), self.cleaned_data.get('password_confirm')) != 0:
            raise ValidationError(u'password mismatch')
        return self.cleaned_data


class ReactivateForm(forms.Form):
    username = forms.SlugField(min_length=4, max_length=16)
    password = forms.CharField(min_length=6, max_length=16, widget=forms.PasswordInput)
    email = forms.EmailField(required=False, max_length=30)
    
    
    def clean_username(self):
        value = self.cleaned_data['username']
        try:
            User.objects.get(username=value)
        except User.DoesNotExist:
            return ValidationError(u'Username "%s" does not exist.' % value)
        raise value
    
def waitActivate(user_profile):
    user = user_profile.user
    salt = hashlib.sha512(str(random.random())).hexdigest()[:5]
    activation_key = hashlib.sha512(salt+user.username).hexdigest()[:30]
    key_expires = datetime.datetime.today() + datetime.timedelta(2)
    # Create and save their user_profile            
    user_profile.key_expires = key_expires 
    user_profile.activation_key = activation_key
    user_profile.save()
    # Send an email with the confirmation link                                                                                                                      
    email_subject = 'Your Library Management System Account Confirmation'
<<<<<<< HEAD
    email_body = u'''%s, Welcome To FDUCS AI Contest!\n\n
    Please click within 48 hours to activate:\n\n
    http://localhost:8000/confirm/%s/''' % (user.username, user_profile.activation_key)
    send_mail(email_subject, email_body, 'fudancsai@gmail.com', [user.email], fail_silently = False)
=======
    email_body = u'''%s, Welcome To Library Management System!\n\n
    Please click within 48 hours to activate:\n\n
    http://localhost:8000/confirm/%s/''' % (user.username, user_profile.activation_key)
    send_mail(email_subject, email_body, 'accounts@library.com', [user.email], fail_silently = False)
>>>>>>> a1de5c51978df166ab3cad8042db56267130c32d

def register(request):
    t = 'registration/register.html'
    if request.user.is_authenticated():
        return render_to_response(t, {'has_account': True})
    form = RegistrationForm()
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()                                                                                                                                                                                                                                    
            new_profile = UserProfile(user=new_user)
            waitActivate(new_profile)
            return render_to_response(t, {'success': True, 'email':new_user.email})
    return render_to_response(t, {'form': form })

def confirm(request, activation_key):
    t = 'registration/confirm.html'
    if request.user.is_authenticated():
        return render_to_response(t, {'has_account': True})
    user_profile = get_object_or_404(UserProfile,
                                     activation_key=activation_key)
    if user_profile.key_expires < datetime.datetime.today():
        return render_to_response(t, {'expired': True})
    user = user_profile.user
    user.is_active = True
    user.save()
    return render_to_response(t, {'success': True})

def reactivate(request):
    t = 'registration/reactivate.html'
    if request.user.is_authenticated():
        return render_to_response(t, {'has_account': True})
    form = ReactivateForm()
    if request.POST:
        form = ReactivateForm(request.POST)
        if form.is_valid():
            d = form.cleaned_data
            user = authenticate(username=d['username'], password=d['password'])
            if user is not None:
                if user.is_active:
                    return render_to_response(t, {'activated': True})
                if len(d['email']) > 0:
                    user.email = d['email']
                    user.save()
                user_profile = user.get_profile()
                waitActivate(user_profile)
                return render_to_response(t, {'success': True, 'email': user.email})
            else:
                return render_to_response(t, {'illegal': True, 'form': form})
    return render_to_response(t, {'form': form})