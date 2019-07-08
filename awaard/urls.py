from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.landing_page, name='home'),
    url(r'^edit/$', views.edit_profile, name="edit_profile"),
    url(r'^profile/(\d+)', views.profile, name="profile"),
    # url(r'^search/', views.search_results, name='search_results')
    url(r'^api/projects/$',views.ProjectList.as_view()),
    url(r'^api/profile/$',views.ProfileList.as_view()),
    url(r"^new/project/$",views.new_post, name='new_post'),
    url(r'^project/(\d+)',views.single_post, name="single_post"),
]
