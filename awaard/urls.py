from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.join_hood, name="home"),
    url(r'^edit/$', views.edit_profile, name="edit_profile"),
    url(r'^profile/(\d+)', views.profile, name="profile"),
    url(r'^nb/$',views.new_biz, name="new_biz"),
    url(r'^nh/$',views.new_hood, name= "new_hood"),
    url(r'^hood/(\d+)',views.hood,name="hood"),
    # url(r'^search/', views.search_results, name='search_results'),
    url(r'^api/projects/$',views.PostList.as_view()),
    url(r'^api/profile/$',views.ProfileList.as_view()),
    url(r"^new/project/$",views.new_post, name='new_post'),
    url(r'^project/(\d+)',views.single_post, name="single_post"),
]
