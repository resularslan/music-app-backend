# VibeFlow Proxy Backend 🎵

> ✨ **Developer Note:** This entire project was brought to life through **Vibe Coding**! 🌊 By leveraging AI for rapid prototyping, complex system design, and architecture, the focus was kept purely on product vision, UX, and solving real problems without getting bogged down by boilerplate code. Even this text is generated with AI.
> ❗ **Warning:** This project is provided for educational and research purposes only. The author assumes no responsibility or liability for any misuse of this software, violation of YouTube’s Terms of Service, or any other damages or consequences arising from its use. Use at your own risk.

This project is the custom backend developed for the VibeFlow music app. It acts as a high-speed proxy that overcomes YouTube bot protections and provides seamless, lightning-fast audio streaming and downloading.

## 🚀 Tech Stack
* **Python 3.10+**
* **FastAPI** (High-performance API server)
* **yt-dlp** (Audio data extraction and protection skipper)
* **aria2c & FFmpeg** (Multi-threaded download accelerators for lightning-fast audio processing)
* **Docker** (Containerized for seamless cloud deployment)

---

## ⚠️ Important Note on Cloud Deployment & YouTube Anti-Bot

This architecture is highly performant and works flawlessly when hosted on a **residential network** (like your local PC during development or a home server/Raspberry Pi). 

However, if you are planning to deploy this API directly to popular cloud platforms (such as Render, Heroku, AWS, or DigitalOcean), please be aware of YouTube's aggressive IP blocking:

* **The Issue:** YouTube frequently flags and blocks traffic coming from known datacenter IPs. You might encounter `403 Forbidden` errors, `Sign in to confirm you're not a bot` messages, or unexpected extraction failures.
* **Why it happens:** This is not a bug in the code; it is a network-level restriction enforced by Google.

### 💡 Cloud Deployment Solutions
If you want to host this backend on a cloud server successfully, you will likely need to configure one of the following:
1. **Provide a `cookies.txt`:** Pass a valid YouTube cookie file to `yt-dlp` to authenticate the session.
2. **Use Residential Proxies:** Route the `yt-dlp` traffic through rotating residential proxies.
3. **IPv6 Routing:** Some developers bypass blocks by forcing IPv6 connections.

*If you deploy this successfully on a cloud provider using a specific proxy or cookie configuration, **Pull Requests are highly welcome!** Feel free to fork, experiment, and share your workarounds.*

---

## ⚙️ Installing (Developer Environment)
1. Clone the repo.
2. Create the virtual environment: `python -m venv venv`
3. Install the dependencies: `pip install -r requirements.txt`
4. Start the server: `uvicorn main:app --reload`
