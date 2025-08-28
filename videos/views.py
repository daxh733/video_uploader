from urllib import response
import django
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import gridfs
from bson import ObjectId
from .mongo_client import db
from .models import Video 
from django.shortcuts import render,redirect
from django.http import StreamingHttpResponse, Http404

fs = gridfs.GridFS(db)

@csrf_exempt
def upload_video(request):
    if request.method == 'POST':
        video_file = request.FILES.get("video")
        title = request.POST.get("title")

        if not video_file:
            return JsonResponse({"error": "No video file uploaded"}, status=400)

        # store file in GridFS
        file_id = fs.put(video_file, filename=video_file.name)

        # save meta in videos collection
        videos = db["videos"]
        videos.insert_one({
            "title": title,
            "file_id": file_id
        })

        return JsonResponse({
            "msg": "Video Uploaded Successfully",
            "file_id": str(file_id)
        })
    return JsonResponse({"msg": "Invalid Request"}, status=400)


def list_videos(request):
    videos = list(db.videos.find({}))
    for v in videos:
        v["_id"] = str(v["_id"])
        if "file_id" in v:
            v["file_id"] = str(v["file_id"])
    return JsonResponse(videos, safe=False)


def video_list(request):
    videos = list(db.videos.find({}))
    filtered_videos = []
    for v in videos:
        v["_id"] = str(v["_id"])
        if "file_id" in v and v["file_id"]:
            v["file_id"] = str(v["file_id"])
            filtered_videos.append(v)
    return render(request, 'videos/video_list.html', {'videos': filtered_videos})


def serve_video(request, file_id):
    try:
        file_obj=fs.get(ObjectId(file_id))
        response=StreamingHttpResponse(file_obj,content_type="video/mp4")
        response['Content-Disposition']=f'inline;filename="{file_obj.filename}"'
        return response
    except Exception as e:
        raise Http404("Video not found")
    
def upload_video_web(request):
    if request.method=='POST':
        video_file=request.FILES.get("video")
        title=request.POST.get("title")

        if not title:
           return render(request, 'videos/upload_video.html', {'error': "No title provided"})
        if not video_file.content_type.startswith('video/'):
            return render(request, 'videos/upload_video.html', {'error': "Only video files are allowed."})

       # store file in GridFS
        file_id = fs.put(video_file, filename=video_file.name)

       # save meta in videos collection
        videos = db["videos"]
        videos.insert_one({
           "title": title,
           "file_id": file_id
       })

        return redirect('video_list')

    return render(request, 'videos/upload_video.html')