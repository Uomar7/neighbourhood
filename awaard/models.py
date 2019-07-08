from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=40)
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_pic = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.fname

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


    @classmethod
    def get_profiles(cls):
        all_profiles = cls.objects.all()
        return all_profiles

    @classmethod
    def get_profile_by_id(cls, id):
        profile = cls.objects.get(id= id)
        return profile

    @classmethod
    def search_profile(cls, search_item):
        sought_prof = cls.objects.filter(name__username= search_item)
        return sought_prof


class Post(models.Model):
    title = models.CharField(max_length=100)
    post_image = models.ImageField(upload_to='images/')
    post_description = models.TextField()
    post = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="posts")
    posted = models.DateTimeField(auto_now_add=True)
    neigh = models.ForeignKey('Neighbourhood', related_name='posts')
    # new column comments added below
    # new column called usabilityrate

    def __str__(self):
        return self.title

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def get_post(cls):
        all_posts = cls.objects.all()
        return all_posts
    @classmethod
    def get_post_by_id(cls, id):
        post = cls.objects.get(id=id)
        return post

class Neighbourhood(models.Model):
    name = models.CharField(max_length = 40)
    member = models.ForeignKey(Profile, null = True, related_name="neighbourhoods")
    police = models.CharField(max_length=80)
    health = models.CharField(max_length=80)
    p_no = models.CharField(max_length=20)
    h_no = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    def save_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

    @classmethod
    def get_all_neighbourhoods(cls):
        all_neighbourhoods = cls.objects.all()
        return all_neighbourhoods

class Business(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length = 80)
    location = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def get_all_businesses(cls):
        all_businesses = cls.objects.all()
        return all_businesses
    
class Comment(models.Model):
    review = models.CharField(max_length=400, blank=False) # automatically adds a new column on the project class called comments
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.review

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_comment(cls):
        all_comments = cls.objects.all()
        return all_comments

    @classmethod
    def get_comment_by_id(cls, id):
        comment = cls.objects.get(id=id)
        return comment


    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(username=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
