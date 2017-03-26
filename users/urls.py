from django.conf.urls import url

from .views import login_view, profile_view, logout_user

urlpatterns = [
    url(r'^profile/$', profile_view, name='profile'),
    url(r'^logout/$', logout_user, name='logout'),
    #url(r'^register/$', register_view, name='profile'),
    url(r'^', login_view, name='login'),
]