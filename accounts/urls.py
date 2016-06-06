from django.contrib.auth.views import login
from django.conf.urls import url

urlpatterns = [
    url(r'^login/$', login),
]