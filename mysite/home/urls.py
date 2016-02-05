from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: domain.com/
    url(r'^$', views.index, name='index'),
]