from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt
from django.db import transaction
from django.contrib.auth.decorators import login_required
from .models import Profile, Project, Comment, UsabilityRate, ContentRate, DesignRate
from .forms import ProfileForm, CommentForm, ProjectForm, UsabilityRateForm,ContentRateForm,DesignRateForm
from django.contrib.auth.models import User
# creating an api view for my models.
from .permissions import IsAdminOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer,CommentSerializer
from django.http import JsonResponse
from rest_framework import status

# @login_required(login_url='/accounts/login/')
def landing_page(request):
    projects = Project.objects.all()
    # project_comments = Project.objects.get(pk = id)
    # all_comments = project_comments.comments.all()
    return render(request, 'all-temps/index.html',{"projects":projects})

@login_required(login_url='/accounts/login/')
def new_project(request):

    current_user =Profile.objects.get(username=request.user)
    if request.method == "POST":
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            proj = form.save(commit=False)
            proj.profile = current_user
            proj.save()
        
        return redirect(landing_page)
    else:
        form = ProjectForm()
    return render(request,"all-temps/new_project.html",{"form":form})


@login_required(login_url='/accounts/login/')
def profile(request,id):
    current_user = request.user
    profile = Profile.objects.get(username=id)
    projectz = profile.projects.all()
    print(projectz)
    return render(request, 'all-temps/profile.html',{"projectz":projectz,"profile":profile})

@transaction.atomic
def edit_profile(request):
    current_user = Profile.objects.get(username = request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance = current_user)
        if form.is_valid():
            form.save()

            return redirect('profile',current_user.id)
    
    else:
        form = ProfileForm(instance = request.user.profile)

    return render(request, "all-temps/edit_profile.html", {"form":form})

@login_required(login_url='/accounts/login/')
def single_project(request, project_id):
    current_user = Profile.objects.get(username = request.user)
    # all forms

    form = CommentForm()
    design_form = DesignRateForm()
    usability_form = UsabilityRateForm()
    contentform = ContentRateForm()
    # endforms
    
    project = Project.objects.get(id=project_id)
    comments = project.comments.all()

    try:
        project = Project.objects.get(id=project_id)
    except DoesNotExist:
        raise Http404

    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.posted_by = request.user
            comment.project = project

            comment.save()
            return redirect('single_project', project_id)
    else:
        form = CommentForm()

# form for design rate.
    if request.method == 'POST':
        design_form = DesignRateForm(request.POST, request.FILES)
        if design_form.is_valid():
            des = design_form.save(commit = False)
            des.voter = request.user
            des.project = project

            des.save()
    
    else:
        design_form = DesignRateForm()

# checking if the forms saves anything.

    if request.method == 'POST':
        contentform = ContentRateForm(request.POST, request.FILES)
        if contentform.is_valid():
            des = contentform.save(commit=False)
            des.voter = request.user
            des.project = project

            des.save()
        
    else:
        contentform = ContentRateForm()

    if request.method == 'POST':
        usability_form = UsabilityRateForm(request.POST, request.FILES)
        if usability_form.is_valid():
            des = usability_form.save(commit=False)
            des.voter = request.user
            des.project = project

            des.save()

    else:
        usability_form = UsabilityRateForm()

    design_total = project.design_rates.all()
    print(design_total)
    content_total = project.content_rates.all()
    print(content_total)
    usability_total = project.usability_rates.all()
    print(usability_total)
    # usability average
    all = []
    for item in list(usability_total):
        all.append(int(item.rating))
    
    average_use = sum(all)/len(all)
    use_total = str("{:.2f}".format(average_use))

    # Design average
    dall = []
    for ite in list(design_total):
        dall.append(int(ite.rating))
    
    average_des = sum(dall)/len(dall)
    datall = str("{:.2f}".format(average_des))

    # Content Average
    call = []
    for it in list(content_total):
        call.append(int(it.rating))

    average_con = sum(call)/len(call)
    coll = str("{:.2f}".format(average_con))



    return render(request, "all-temps/project.html",{"project":project,"form":form,"comments":comments,"useform":usability_form,"desform":design_form,"contform":contentform,"ct":coll,"dt":datall,"ut":use_total})

# Models APIView
class ProjectList(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)

        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers = ProjectSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileList(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, format=None):
        all_Profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_Profiles, many=True)

        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentList(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, format=None):
        all_comments = Comment.objects.all()
        serializers = CommentSerializer(all_comments,many=True)

        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get_project(self, pk):
        try:
            return Project.objects.get(pk = pk)
        
        except Project.DoesNotExist:
            return Http404
    
    def put(self, request, pk, format=None):
        project = self.get_project(pk)
        serializers = ProjectSerializer(project, request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        project = self.get_project(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProfileDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get_profile(self, pk):
        try:
            return Profile.objects.get(pk=pk)

        except Profile.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile)

        return Response(serializers.data)

    def put(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile, request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profile = self.get_profile(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get_comment(self, pk):
        try:
            return Comment.objects.get(pk=pk)

        except Comment.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        comment = self.get_comment(pk)
        serializers = CommentSerializer(comment)

        return Response(serializers.data)

    def put(self, request, pk, format=None):
        comment = self.get_comment(pk)
        serializers = CommentSerializer(comment, request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        comment = self.get_comment(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
