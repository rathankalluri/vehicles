from django.conf.urls import url
from . import views

urlpatterns = [
    # Home Page of App
    url(r'^$', views.index, name='index'),
    url(r'^excelgen/', views.excelgen, name='excelgen'),
    url(r'^create_new/', views.create_new, name="create_new"),
    url(r'^update_new/', views.update_new, name="update_new"),
    url(r'^delete_new/', views.delete_new, name="delete_new"),
]
