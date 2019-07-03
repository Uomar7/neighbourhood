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


class Project(models.Model):
    title = models.CharField(max_length=100)
    project_image = models.ImageField(upload_to='images/')
    project_description = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="projects")
    link = models.URLField()
    posted = models.DateTimeField(auto_now_add=True)
    # new column comments added below
    # new column called usabilityrate

    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def get_project(cls):
        all_projects = cls.objects.all()
        return all_projects

    @classmethod
    def get_project_by_id(cls, id):
        project = cls.objects.get(id=id)
        return project

class Comment(models.Model):
    review = models.CharField(max_length=400, blank=False) # automatically adds a new column on the project class called comments
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments')
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

CHOICES = (
    (0,'0'),
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
    project = models.ForeignKey(Project,related_name='design_rates')
    voted_at = models.DateTimeField(auto_now_add=True)
    voter = models.ForeignKey(User)
    rating = models.IntegerField(default=0, choices=CHOICES, null=True)

    def __str__(self):
        return str(self.rating)

class ContentRate(models.Model):
    project = models.ForeignKey(Project,related_name='content_rates')
    voted_at = models.DateTimeField(auto_now_add=True)
    voter = models.ForeignKey(User)
    rating = models.IntegerField(default=0, choices=CHOICES, null=True)

    def __str__(self):
        return str(self.rating)

class UsabilityRate(models.Model):
    project = models.ForeignKey(Project,related_name='usability_rates')
    voted_at = models.DateTimeField(auto_now_add=True)
    voter = models.ForeignKey(User)
    rating = models.IntegerField(default = 0,choices=CHOICES, null=True)

    def __str__(self):
        return str(self.rating)

    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(username=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
