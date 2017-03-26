from django.conf.urls import url

from .views import index, create_blog_post,blog_detail,blog_detailform


urlpatterns = [
    url(r'^create/$', create_blog_post, name='create'),
    #url(r'^blog-detail/(.*)/$', blog_detail,name='blog-detail'),
    url(r'^blog-detail/(.*)/$', blog_detailform, name='blog-detail'),
    url(r'^$', index, name='index'),
]
