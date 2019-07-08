from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt
from django.db import transaction
from django.contrib.auth.decorators import login_required
from .models import Profile, Post, Comment, Neighbourhood, Business
from .forms import ProfileForm, CommentForm, PostForm, NeighbourhoodForm, BusinessForm
from django.contrib.auth.models import User
# creating an api view for my models.
from .permissions import IsAdminOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer, PostSerializer, CommentSerializer, BusinessSerializer, NeighbourhoodSerializer
from rest_framework import status


@login_required(login_url='/accounts/login/')
def landing_page(request):
    posts = Post.objects.all()

    return render(request, 'all-temps/index.html', {"posts": posts})


@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = Profile.objects.get(username=request.user)
    loc = Neighbourhood.objects.get(member=current_user)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            proj = form.save(commit=False)
            proj.post = current_user
            proj.neigh = loc
            proj.save()

        return redirect(hood, loc.id)
    else:
        form = PostForm()
    return render(request, "all-temps/new_project.html", {"form": form})


@login_required(login_url='/accounts/login/')
def profile(request, id):
    current_user = request.user
    profile = Profile.objects.get(username=id)
    postz = profile.posts.all()

    return render(request, 'all-temps/profile.html', {"postz": postz, "profile": profile})


@transaction.atomic
def edit_profile(request):
    current_user = Profile.objects.get(username=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save()

            return redirect('profile', current_user.id)

    else:
        form = ProfileForm(instance=request.user.profile)

    return render(request, "all-temps/edit_profile.html", {"form": form})


@login_required(login_url="/accounts/login/")
def new_biz(request):
    profile = Profile.objects.get(username=request.user)
    loc = Neighbourhood.objects.get(member=profile)

    if request.method == "POST":
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            biz = form.save(commit=False)
            biz.owner = request.user
            biz.location = loc
            biz.save()
            return redirect('hood', loc.id)
    else:
        form = BusinessForm()
    return render(request, "all-temps/new_biz.html", {"form": form})


@login_required(login_url="/accounts/login/")
def new_hood(request):
    current_user = request.user
    profile = Profile.objects.get(username=current_user)
    if request.method == "POST":
        form = NeighbourhoodForm(request.POST, request.FILES)
        if form.is_valid():
            neigh = form.save(commit=False)
            neigh.member = profile
            neigh.save()

            return redirect('hood', neigh.id)
    else:
        form = NeighbourhoodForm()
    return render(request, "all-temps/new_hood.html", {"form": form})


@login_required(login_url="/accounts/login/")
def join_hood(request):
    hoods = Neighbourhood.objects.all()
    return render(request, "all-temps/j_hood.html", {"hoods": hoods})


@login_required(login_url="/accounts/login/")
def hood(request, id):
    hood = Neighbourhood.objects.get(id=id)
    posts = hood.posts.all()
    businesses = Business.objects.filter(location = id).all()
    print(businesses)

    return render(request, "all-temps/hood.html", {"hood": hood, "posts": posts, "biziz":businesses})


@login_required(login_url='/accounts/login/') 
def single_post(request, post_id):
    current_user = Profile.objects.get(username=request.user)
    # all forms
    form = CommentForm()
    post = Post.objects.get(id=post_id)
    comments = post.comments.all()

    try:
        post = Post.objects.get(id=post_id)
    except DoesNotExist:
        raise Http404

    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.posted_by = request.user
            comment.post = post

            comment.save()
            return redirect('single_post', post_id)
    else:
        form = CommentForm()

    return render(request, "all-temps/project.html", {"post": post, "form": form, "comments": comments})

# Models APIView


class PostList(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, format=None):
        all_posts = Post.objects.all()
        serializers = PostSerializer(all_posts, many=True)

        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = PostSerializer(data=request.data)
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
        serializers = CommentSerializer(all_comments, many=True)

        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get_post(self, pk):
        try:
            return Post.objects.get(pk=pk)

        except Post.DoesNotExist:
            return Http404

    def put(self, request, pk, format=None):
        post = self.get_post(pk)
        serializers = PostSerializer(post, request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_post(pk)
        post.delete()
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
