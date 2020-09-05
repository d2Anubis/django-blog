from django.conf.urls import url
from . import views

app_name = 'users'

urlpatterns = [
    url(r'^signup/$', views.sign, name="signup"),
    url(r'^about/$', views.about, name="about"),
    url(r'^login/$', views.logging_in, name="login"),
    url(r'^logout/$', views.logging_out, name="logout"),
    url(r'^(?P<sub>[\w-]+)/$', views.topic, name="topic"),
]
