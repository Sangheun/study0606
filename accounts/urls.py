from django.contrib.auth.views import login
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', login),
    url(r'^signup/$', views.signup),
]