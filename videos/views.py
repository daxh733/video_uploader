from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import gridfs
from bson import ObjectId
from .mongo_client import db

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
