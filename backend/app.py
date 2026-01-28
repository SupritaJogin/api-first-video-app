from flask import Flask
from routes.auth import auth_bp
from routes.video import video_bp

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret123"

# Register blueprints
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(video_bp)

@app.route("/")
def home():
    return {"message": "Backend running successfully"}

if __name__ == "__main__":
    app.run(debug=True)
