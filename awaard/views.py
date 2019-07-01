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
            # proj.user = current_user
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
    form = CommentForm()
    project = Project.objects.get(id=project_id)
    comments = project.comments.all()

    try:
        project = Project.objects.get(id=project_id)
    except DoesNotExist:
        raise Http404

    # print(CommentForm)
    # if request.method == "POST":
    #     form = CommentForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         comment = form.save(commit=False)
    #         comment.posted_by = request.user

    #         comment.save()    
    return render(request, "all-temps/project.html",{"project":project,"form":form,"comments":comments})

def user_comment(request,project_id):
    review = request.POST.get('review')
    posted_by = request.user
    project = Project.objects.get(id = project_id)

    comment = Comment(review=review,posted_by=posted_by,project=project)
    comment.save()
    data = {'success':'You Have Successfully Reviewed The Project'}
    return JsonResponse(data)



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
