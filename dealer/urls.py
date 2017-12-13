from django.conf.urls import url
from . import views

urlpatterns = [
    # Home Page of App
    url(r'^$', views.index, name='index'),
]
