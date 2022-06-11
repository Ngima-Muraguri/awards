from .models import Profile, Projects
from django import forms
from django.contrib.auth.models import User


class PostProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = ['posted_by', 'date_posted']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


class UpdateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


class UpdateUser(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        exclude = ['username']