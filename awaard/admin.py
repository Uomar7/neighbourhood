from django.contrib import admin
from .models import Profile,Post,Business,Comment,Neighbourhood

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Business)
admin.site.register(Neighbourhood)