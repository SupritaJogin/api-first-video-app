🎯 Assignment Goal

Build a React Native app that acts as a thin client and communicates entirely with a Flask backend. The app fetches videos from the backend and does not expose YouTube URLs directly.

🏗️ System Architecture
React Native App  →  Flask API  →  MongoDB
                         ↓
                      YouTube


The mobile app only: calls APIs, stores JWT, renders data, sends user actions.

All business logic, authentication, and video abstraction are handled in the backend.

💻 Backend Setup (Flask + MongoDB)
Requirements

Python 3.11+

pip / venv

MongoDB running locally or via Atlas

Install dependencies
cd backend
python -m venv venv
venv\Scripts\activate        # On Windows
pip install -r requirements.txt

Run the backend
python app.py


Backend will run at http://127.0.0.1:5000

Test endpoints with curl or Postman:

curl -X POST http://127.0.0.1:5000/auth/login -H "Content-Type: application/json" -d "{\"username\":\"admin\",\"password\":\"1234\"}"
curl http://127.0.0.1:5000/dashboard
curl http://127.0.0.1:5000/video/1/stream

📱 Frontend Setup (React Native + Expo)
Requirements

Node.js 18+

npm

Expo Go (Android/iOS)

Install dependencies & start app
cd VideoAppExpo
npm install
npx expo start


Scan the QR code in Expo Go or open in a web browser

Login with backend credentials:

Username: admin

Password: 1234

Dashboard displays 2 video tiles. Click a tile to play video.

🔐 Auth Flow

User logs in via /auth/login → receives JWT

JWT is stored securely in the app

App calls /dashboard and /video/<id>/stream with JWT

Backend validates JWT and returns data

🎥 Video Abstraction

Backend does not return raw YouTube URLs

Example response:

{
  "playback_url": "https://www.youtube.com/embed/abc123xyz",
  "video_id": "abc123xyz"
}


App plays videos inside a WebView without exposing YouTube links

🗃️ Database Models

User

{
  "id": 1,
  "name": "Admin",
  "email": "admin@example.com",
  "password_hash": "...",
  "created_at": "..."
}


Video

{
  "id": 1,
  "title": "How Startups Fail",
  "description": "Lessons from real founders",
  "youtube_id": "abc123xyz",
  "thumbnail_url": "...",
  "is_active": true
}

✅ Features Completed

JWT authentication (login, profile, logout)

Dashboard fetching videos

Video playback with URL abstraction

React Native thin client

Separation of frontend and backend logic

📌 How to Run Full System

Start MongoDB

Start Flask backend (python app.py)

Start React Native frontend (npx expo start)

Use Expo Go to scan QR and test app

