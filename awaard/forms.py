from django import forms
from .models import Profile, Project, Comment, UsabilityRate, DesignRate, ContentRate
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ["username"]


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['posted','profile']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # exclude = ['posted_by', 'project']
        fields = ['review']
        widget = {
            'review': forms.TextInput(attrs={
                'id': 'comment-text',
                'required': True,
                'placeholder': 'Write Your Remark'
            })
        }


class UsabilityRateForm(forms.ModelForm):
    class Meta:
        model = UsabilityRate
        fields = ['rating']


class DesignRateForm(forms.ModelForm):
    class Meta:
        model = DesignRate
        fields = ['rating']


class ContentRateForm(forms.ModelForm):
    class Meta:
        model = ContentRate
        fields = ['rating']
