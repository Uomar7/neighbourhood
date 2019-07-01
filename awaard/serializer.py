from rest_framework import serializers
from .models import Profile,Project,Comment

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("first_name","last_name","bio","profile_pic")

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("title","project_image","project_description","link")

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("review")