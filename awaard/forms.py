from django import forms
from django.forms import TextInput, CharField,Textarea
from .models import Profile, Post, Comment, Business, Neighbourhood
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ["username"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ["post","posted","neigh"]


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
        widgets = {
            'p_no': TextInput(attrs={
                'placeholder':'Police Phone Address'
            }),
            'police':TextInput(attrs={
                'placeholder':'Police Name'
            }),
            'h_no': TextInput(attrs={
                'placeholder':'Health Center Phone Address'
            }),
            'health':TextInput(attrs={
                'placeholder':'Hospital Name'
            })
        }