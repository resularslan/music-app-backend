from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import yt_dlp

app = FastAPI(title="Music App Proxy API 🎵")

# KORS (CORS) Ayarları: Flutter uygulamamızın (veya tarayıcının) bu API'ye 
# güvenlik engeline takılmadan istek atabilmesini sağlar.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Geliştirme aşamasında her yere açık
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Sunucu tıkır tıkır çalışıyor! Hoş geldin."}

@app.get("/search")
def search_youtube(query: str, max_results: int = 15):
    """
    Kullanıcının gönderdiği metni YouTube'da arar ve sonuçları liste olarak döndürür.
    """
    if not query:
        raise HTTPException(status_code=400, detail="Arama metni boş olamaz!")

    # yt-dlp için özel arama ayarları
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'extract_flat': True, # ÇOK ÖNEMLİ: Videoları indirme, sadece başlık/kapak bilgilerini çek
        'quiet': True,        # Terminali gereksiz loglarla doldurma
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # yt-dlp'nin arama komutu: ytsearch[SAYI]:[KELİME]
            search_str = f"ytsearch{max_results}:{query}"
            info = ydl.extract_info(search_str, download=False)
            
            if 'entries' not in info:
                return {"results": []}

            results = []
            for entry in info['entries']:
                # YouTube'dan gelen ham veriyi, Flutter'ın sevdiği temiz JSON formatına çeviriyoruz
                
                # Kapak fotoğrafını al (Bazen liste, bazen string gelebiliyor)
                thumbnails = entry.get('thumbnails', [])
                thumbnail_url = thumbnails[0]['url'] if thumbnails else "https://via.placeholder.com/150"
                
                results.append({
                    "id": entry.get('id'),
                    "title": entry.get('title'),
                    "author": entry.get('uploader', 'Bilinmeyen Sanatçı'),
                    "thumbnail": thumbnail_url,
                    "duration": entry.get('duration', 0)
                })
            
            return {"results": results}
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"YouTube araması sırasında hata: {str(e)}")
    
@app.get("/stream/{video_id}")
def stream_song(video_id: str):
    """
    Gönderilen YouTube Video ID'sinin arka planda korumalarını aşarak
    doğrudan çalınabilir temiz .m4a ses linkini bulur ve oynatıcıyı oraya yönlendirir.
    """
    if not video_id:
        raise HTTPException(status_code=400, detail="Video ID boş olamaz!")

    # Android'in ve just_audio'nun en sevdiği, 403 hatasını en az veren format: m4a (mp4 ses)
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'quiet': True,
        'extractor_args': {
                'youtube': {
                    'client': ['android', 'ios']
                }
            }
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Sadece videonun meta verilerini ve gizli akış linkini alıyoruz (bilgisayara dosya indirmiyoruz)
            info = ydl.extract_info(f"https://www.youtube.com/watch?v={video_id}", download=False)
            
            audio_url = info.get('url')
            if not audio_url:
                raise HTTPException(status_code=404, detail="Ses akışı bulunamadı.")
            
            # Bulunan gizli ve temiz ses linkine yönlendir (HTTP 307 Temporary Redirect)
            return RedirectResponse(url=audio_url)
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Akış çekilirken hata: {str(e)}")