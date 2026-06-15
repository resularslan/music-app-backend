# Music App Proxy Backend 🎵

This project is developed for a music app. It is a proxy backend that can overcome Youtube bot protections and provide audio streaming.

## 🚀 Techs
* **Python 3.14.5**
* **FastAPI** (High performance API server)
* **yt-dlp** (Audio data provider and protection skipper)

## ⚙️ Installing (Developer Environment)
1. Clone the repo.
2. Create the viritual environment: `python -m venv venv`
3. Install the dependencies: `pip install -r requirements.txt`
4. Start the server: `uvicorn main:app --reload`