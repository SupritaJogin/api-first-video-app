from flask import Blueprint, jsonify

video_bp = Blueprint('video', __name__)

videos = [
    {
        "id": 1,
        "title": "How Startups Fail",
        "description": "Lessons from real founders",
        "youtube_id": "abc123xyz",
        "thumbnail_url": "https://img.youtube.com/vi/abc123xyz/0.jpg",
        "is_active": True
    },
    {
        "id": 2,
        "title": "AI in 2026",
        "description": "Future of AI explained",
        "youtube_id": "def456uvw",
        "thumbnail_url": "https://img.youtube.com/vi/def456uvw/0.jpg",
        "is_active": True
    }
]

@video_bp.route("/dashboard", methods=["GET"])
def dashboard():
    active_videos = [v for v in videos if v["is_active"]][:2]
    for v in active_videos:
        v["video_id"] = v["youtube_id"]
        del v["youtube_id"]
    return jsonify(active_videos)

@video_bp.route("/video/<id>/stream", methods=["GET"])
def stream_video(id):
    video = next((v for v in videos if str(v["id"]) == id), None)
    if not video:
        return jsonify({"message":"Video not found"}), 404
    stream_url = f"https://www.youtube.com/embed/{video['video_id']}"
    return jsonify({"video_id": video["video_id"], "playback_url": stream_url})
