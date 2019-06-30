from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_pic = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.first_name


class Project(models.Model):
    title = models.CharField(max_length=100)
    project_image = models.ImageField(upload_to='images/', default='award/media/images')
    project_description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.URLField()
    posted = models.DateTimeField(auto_now_add=True)
    # new column comments added below
    # new column called usabilityrate


    def __str__(self):
        return self.title


class Comment(models.Model):
    review = models.CharField(max_length=400)# automatically adds a new column on the project class called comments
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments')
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.review

CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10')
)

class DesignRate(models.Model):
    project = models.ForeignKey(Project,related_name='design_rate')
    voted_at = models.DateTimeField(auto_now_add=True)
    voter = models.ForeignKey(User)
    rating = models.IntegerField(choices=CHOICES, null=True)

class ContentRate(models.Model):
    project = models.ForeignKey(Project,related_name='content_rate')
    voted_at = models.DateTimeField(auto_now_add=True)
    voter = models.ForeignKey(User)
    rating = models.IntegerField(choices=CHOICES, null=True)

class UsabilityRate(models.Model):
    project = models.ForeignKey(Project,related_name='usability_rate')
    voted_at = models.DateTimeField(auto_now_add=True)
    voter = models.ForeignKey(User)
    rating = models.IntegerField(choices=CHOICES, null=True)

    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(username=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
