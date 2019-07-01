from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt
from django.db import transaction
from django.contrib.auth.decorators import login_required
from .models import Profile, Project, Comment, UsabilityRate, ContentRate, DesignRate
from .forms import ProfileForm, CommentForm, ProjectForm, UsabilityRateForm,ContentRateForm,DesignRateForm
from django.contrib.auth.models import User
# creating an api view for my models.
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer,CommentSerializer

@login_required(login_url='/accounts/login/')
def landing_page(request):
    projects = Project.objects.all()
    # project_comments = Project.objects.get(pk = id)
    # all_comments = project_comments.comments.all()
    return render(request, 'all-temps/index.html',{"projects":projects})

class ProjectList(APIView):
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)

        return Response(serializers.data)

class ProfileList(APIView):
    def get(self, request, format=None):
        all_Profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_Profiles, many=True)

        return Response(serializers.data)

class CommentList(APIView):
    def get(self, request, format=None):
        all_comments = Comment.objects.all()
        serializers = CommentSerializer(all_comments,many=True)