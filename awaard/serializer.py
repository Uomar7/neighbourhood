from rest_framework import serializers
from .models import Profile,Post,Comment,Business,Neighbourhood

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("id","first_name","last_name","bio","profile_pic")

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id","title","post_image","post_description")

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id","review")

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ("id","name","police","health","p.no","h.no")

class NeighbourhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighbourhood
        fields = ("id","name")