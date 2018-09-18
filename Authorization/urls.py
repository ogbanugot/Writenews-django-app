from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from Authorization import views 


urlpatterns = [
    url(r'^login/$', views.login_user, name='auth-login'),
    url(r'^logout/$', views.logout_user, name='auth-logout'),
    url(r'^signup/$', views.sign_up, name='auth-signup'),
    ]

