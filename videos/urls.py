from django.urls import path
from . import views


urlpatterns = [
    path("upload/", views.upload_video, name="upload_video"),  # API endpoint
    path("upload-web/", views.upload_video_web, name="upload_video_web"),  # Web form
    path("list/", views.list_videos, name="list_videos"),
    path('show/', views.video_list, name='video_list'),
    path('stream/<str:file_id>/', views.serve_video, name='serve_video'),
]

    


