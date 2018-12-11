from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.upload_file, name='upload_file'),
]
