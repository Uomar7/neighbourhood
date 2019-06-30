from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt
from django.db import transaction
from django.contrib.auth.decorators import login_required
from .models import Profile, Project, Comment, UsabilityRate, ContentRate, DesignRate
from .forms import ProfileForm, CommentForm, ProjectForm, UsabilityRateForm,ContentRateForm,DesignRateForm
from django.contrib.auth.models import User

@login_required(login_url='/accounts/login/')
def landing_page(request):
    projects = Project.objects.all()
    project_comments = Project.objects.get(pk = id)
    all_comments = project_comments.comments.all()
