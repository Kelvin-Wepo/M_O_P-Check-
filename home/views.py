from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
from .models import ObesityData

import pandas as pd
from datetime import date

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import AppointmentForm, MentalDisorderForm, pcosDisorderForm, AppointmentDataForm, obesityDisorderForm
from .models import Receipt, UserProfile, userHistory, DoctorUser, AppointmentData
from django.contrib.auth.models import User
from django import forms


import pandas as pd
import joblib
import tensorflow as tf
import numpy as np
from django.utils import timezone
import json

from django.contrib import messages

mental_disorder_model = joblib.load('static/models/mental_disorder_prediction.pkl')
mental_disorder_encoder = joblib.load('static/encoders/mental_disorder_encoder.pkl')
mental_disorder_output_encoder = joblib.load('static/encoders/mental_disorder_output_encoder.pkl')
mental_disorder_df = pd.read_csv('static/mentalDisorder.csv')

pcos_model = joblib.load('static/models/pcos_prediction.pkl')

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for CSS Properties
        self.fields['username'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['email'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['first_name'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'col-md-10 form-control'})

        self.fields['username'].help_text = '<span class="text-muted">Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</span>'
        self.fields['email'].help_text = '<span class="text-muted">Required. Inform a valid email address.</span>'
        self.fields['password2'].help_text = '<span class="text-muted">Enter the same password as before, for verification.</span>'
        self.fields['password1'].help_text = '<span class="text-muted"><ul class="small"><li class="text-muted">Your password can not be too similar to your other personal information.</li><li class="text-muted">Your password must contain at least 8 characters.</li><li class="text-muted">Your password can not be a commonly used password.</li><li class="text-muted">Your password can not be entirely numeric.</li></ul></span>' 

class DoctorRegistrationForm(UserRegistrationForm):
    
    phone = forms.CharField(max_length=20)
    specialization = forms.CharField(max_length=100)
    hospital = forms.CharField(max_length=255)
    city = forms.CharField(max_length = 100)
    state = forms.CharField(max_length = 100)
    country = forms.CharField(max_length = 100)
    about = forms.CharField(max_length = 1000)
    education = forms.CharField(max_length = 1000)
    experience = forms.CharField(max_length = 1000)
    languages = forms.CharField(max_length = 1000)
    expertise = forms.CharField(max_length = 1000)

    class Meta:
        model = DoctorUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 
                'phone', 'specialization', 'hospital', 'city', 'state', 'country',
                'about', 'education', 'experience', 'languages', 'expertise']
        db_table = 'doctor_user'

    DoctorUser.groups.field.related_name = 'doctor_groups'
    DoctorUser.user_permissions.field.related_name = 'doctor_user_permissions'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for CSS Properties
        self.fields['username'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['email'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['first_name'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['specialization'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['hospital'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['city'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['state'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['country'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['about'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['education'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['experience'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['languages'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['expertise'].widget.attrs.update({'class': 'col-md-10 form-control'})

        self.fields['username'].help_text = '<span class="text-muted">Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</span>'
        self.fields['email'].help_text = '<span class="text-muted">Required. Inform a valid email address.</span>'
        self.fields['password2'].help_text = '<span class="text-muted">Enter the same password as before, for verification.</span>'
        self.fields['password1'].help_text = '<span class="text-muted"><ul class="small"><li class="text-muted">Your password can not be too similar to your other personal information.</li><li class="text-muted">Your password must contain at least 8 characters.</li><li class="text-muted">Your password can not be a commonly used password.</li><li class="text-muted">Your password can not be entirely numeric.</li></ul></span>' 
        
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        
        try:
            if form.is_valid():
                form.save()
                return redirect('login')
        except:
            form = UserRegistrationForm()
            messages.error(request, "Something went wrong. Try again!")
            
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def doctor_register(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST)
        form2 = UserRegistrationForm(request.POST)
        
        try:
            if form.is_valid():
                form.save()
                form2.save()
                return redirect('doctor_login')
        except:
            form = DoctorRegistrationForm()
            messages.error(request, "Something went wrong. Try again!")
    else:
        form = DoctorRegistrationForm()
    return render(request, 'doctor_register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, "Something went wrong. Try again!")
    return render(request, 'login.html')

