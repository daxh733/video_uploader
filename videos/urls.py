from django.urls import path
from . import views

urlpatterns=[
    path("upload/", views.upload_video, name="upload_video"),
    path("list/", views.list_videos, name="list_videos"),
]