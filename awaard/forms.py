from django import forms
from .models import Profile,Project,Comment,Rate
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ["username"]

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user','posted']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['posted_by','project']

class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        exclude = ['project','voter']