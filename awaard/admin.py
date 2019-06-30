from django.contrib import admin
from .models import Profile,Project,Comment,UsabilityRate,DesignRate,ContentRate

admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(UsabilityRate)
admin.site.register(ContentRate)
admin.site.register(DesignRate)