from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ArticleList.as_view()), #list all articles
    url(r'^(?P<pk>[0-9]+)/$', views.ArticleDetail.as_view()), #get a particular article
    url(r'^users/$', views.UserList.as_view()), #list all writers 
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()), #get a particular writer
]
