from django import forms
from .models import Profile, Post, Comment, Business, Neighbourhood
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ["username"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['posted','profile']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['review']
        widgets = {
            'placeholder':'Write Your Review'
        }

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ["location","owner"]

class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ["member","member"]