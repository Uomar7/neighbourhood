from django import forms
from .models import Profile,Project,Comment,Rate
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ["username"]