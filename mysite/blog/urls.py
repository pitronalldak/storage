from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /blog/
    url(r'^$', views.index, name='index'),
    # ex: /blog/31856/
    url(r'^(?P<post_id>[0-65000]+)/$', views.post, name='post'),
    
]