from django.conf.urls import url
from . import views

app_name = 'articles'

urlpatterns = [
    url(r'^$',views.articles,name="articles"),
    url(r'^create/$', views.create, name="create"),
    url(r'^(?P<slug>[0-9+]+)/$', views.detail, name="detail"),
]
