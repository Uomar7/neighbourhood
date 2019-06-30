from django.contrib import admin
from .models import Profile,Project,Comment,Rate

admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(Rate)