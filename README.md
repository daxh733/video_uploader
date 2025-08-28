# Django MongoDB Video Uploader

A web application to upload, store, and stream videos using Django, MongoDB, and GridFS.  
Users can upload videos via a modern web interface, view all uploaded videos in a responsive gallery, and stream videos directly from the browser.

---

## Features

- Upload video files via a web form (only video files allowed)
- Store videos in MongoDB using GridFS
- List all uploaded videos in a responsive, modern UI
- Stream videos directly from MongoDB to the browser
- Click video titles to open and play in a new tab

---

## Tech Stack

- **Backend:** Django (Python)
- **Database:** MongoDB (with GridFS for file storage)
- **Frontend:** HTML, CSS (custom, responsive)

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure MongoDB

- Make sure MongoDB is running locally or update your `mongo_client.py` with your MongoDB connection string.

### 5. Run the Django development server

```bash
python manage.py runserver
```

### 6. Access the app

- Upload videos: [http://localhost:8000/videos/upload-web/](http://localhost:8000/videos/upload-web/)
- View all videos: [http://localhost:8000/videos/show/](http://localhost:8000/videos/show/)

---

## Project Structure

```
project-root/
├── videos/
│   ├── templates/
│   │   └── videos/
│   │       ├── upload_video.html
│   │       └── video_list.html
│   ├── views.py
│   ├── urls.py
│   └── ...
├── videouploader/
│   ├── settings.py
│   └── urls.py
├── manage.py
└── requirements.txt
```

---


## Notes

- Only video files are accepted for upload (validated by MIME type).
- Videos are stored in MongoDB GridFS, and metadata is stored in the `videos` collection.
- The app is for development/demo use. For production, add authentication, file size limits, and security checks.

---

## License

MIT License

---

## Credits

- [Django](https://www.djangoproject.com/)
- [MongoDB](https://www.mongodb.com/)
- [GridFS](https://docs.mongodb.com/manual/core/gridfs/)

---

**Happy uploading!**
