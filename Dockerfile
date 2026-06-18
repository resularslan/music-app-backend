# Temel Python işletim sistemini alıyoruz
FROM python:3.10-slim

# İndirme hızlandırıcımız (aria2) ve ses dönüştürücü (ffmpeg) sistem programlarını kuruyoruz
RUN apt-get update && apt-get install -y aria2 ffmpeg

# Çalışma klasörümüzü belirliyoruz
WORKDIR /app

# Gerekli Python paketlerini (fastapi, yt-dlp vs.) kuruyoruz
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Tüm kodumuzu kutunun içine kopyalıyoruz
COPY . .

# Sunucuyu Render'ın belirlediği port üzerinden başlatıyoruz
CMD uvicorn main:app --host 0.0.0.0 --port ${PORT:-10000}