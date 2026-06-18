# VibeFlow Proxy Backend 🎵

> ✨ **Developer Note:** This entire project was brought to life through **Vibe Coding**! 🌊 By leveraging AI for rapid prototyping, complex system design, and architecture, the focus was kept purely on product vision, UX, and solving real problems without getting bogged down by boilerplate code. Even this text is generated with AI.

This project is the custom backend developed for the VibeFlow music app. It acts as a high-speed proxy that overcomes YouTube bot protections and provides seamless, lightning-fast audio streaming and downloading.

## 🚀 Tech Stack
* **Python 3.10+**
* **FastAPI** (High-performance API server)
* **yt-dlp** (Audio data extraction and protection skipper)
* **aria2c & FFmpeg** (Multi-threaded download accelerators for lightning-fast audio processing)
* **Docker** (Containerized for seamless cloud deployment)

## ⚙️ Installing (Developer Environment)
1. Clone the repo.
2. Create the virtual environment: `python -m venv venv`
3. Install the dependencies: `pip install -r requirements.txt`
4. Start the server: `uvicorn main:app --reload`