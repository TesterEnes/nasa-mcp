# NASA APIs MCP Server

Bu proje, NASA'nın tüm açık API endpoint'lerini tek bir MCP (Model Context Protocol) sunucusu üzerinden sağlayan kapsamlı bir entegrasyon sistemidir.

## 🚀 Özellikler

### Desteklenen NASA API'leri:
- **APOD** - Astronomy Picture of the Day
- **Asteroids NeoWs** - Near Earth Object Web Service
- **DONKI** - Space Weather Database
- **Earth Imagery** - Landsat 8 Earth imagery
- **EONET** - Earth Observatory Natural Event Tracker
- **EPIC** - Earth Polychromatic Imaging Camera
- **Exoplanet Archive** - Confirmed exoplanets database
- **InSight Mars Weather** - Mars weather data
- **Mars Rover Photos** - Curiosity, Opportunity, Spirit, Perseverance
- **NASA Image Library** - Search NASA's media collection

### Teknik Özellikler:
- **Modüler Yapı** - Her API için ayrı modül
- **Error Handling** - Kapsamlı hata yönetimi ve retry mekanizması
- **Rate Limiting** - API limitlerini aşmamak için akıllı rate limiting
- **Configuration** - Environment variables ile yapılandırma
- **Logging** - Detaylı loglama sistemi
- **MCP Uyumlu** - AI modelleri tarafından kullanılabilir

## 📊 Mevcut MCP Tools

### APOD (Astronomy Picture of the Day)
- `get_astronomy_picture_of_the_day` - Günün astronomi resmi
- `get_apod_date_range` - Tarih aralığında APOD resimleri
- `get_random_apod` - Rastgele APOD resimleri

### Asteroids (Near Earth Objects)
- `get_asteroid_feed` - Yaklaşan asteroidler
- `get_asteroid_by_id` - Belirli asteroid detayları
- `browse_asteroids` - Asteroid veritabanını tarama
- `get_asteroid_statistics` - NEO istatistikleri

### Mars
- `get_mars_weather_data` - Mars hava durumu
- `get_mars_rover_photos_by_sol` - Sol gününe göre rover fotoğrafları
- `get_mars_rover_photos_by_date` - Tarihe göre rover fotoğrafları
- `get_mars_rover_latest_photos` - En son rover fotoğrafları
- `get_mars_rover_manifest` - Rover görev manifestosu

### Earth
- `get_earth_imagery` - Dünya uydu görüntüleri
- `get_earth_assets` - Mevcut Dünya görüntü varlıkları

### EPIC (Earth Polychromatic Imaging Camera)
- `get_epic_natural_images` - Doğal renk Dünya görüntüleri
- `get_epic_enhanced_images` - Geliştirilmiş renk Dünya görüntüleri

### Natural Events
- `get_natural_events` - Doğal afetler ve olaylar
- `get_event_categories` - Olay kategorileri

### Space Weather (DONKI)
- `get_solar_flares` - Güneş patlamaları
- `get_coronal_mass_ejections` - Koronal kütle atımları

### Media & Exoplanets
- `search_nasa_media` - NASA medya kütüphanesi arama
- `get_confirmed_exoplanets` - Onaylanmış exoplanetler
- `search_exoplanets_by_name` - İsme göre exoplanet arama
- `get_habitable_exoplanets` - Yaşanabilir exoplanetler

## 🛠️ Kurulum

### 1. Gereksinimler
```bash
pip install -r requirements.txt
```

### 2. Konfigürasyon
```bash
# .env dosyası oluştur
cp .env.example .env

# NASA API anahtarını düzenle
nano .env
```

### 3. Çalıştırma

#### Doğrudan Çalıştırma
```bash
python server.py
```

#### Docker ile Çalıştırma
```bash
# Docker image oluştur
docker build -t nasa-apis-mcp .

# Konteyner çalıştır
docker run nasa-apis-mcp

# Kendi API anahtarınızla çalıştır
docker run -e NASA_API_KEY=your_api_key_here nasa-apis-mcp
```

#### Test Etme
```bash
# Tüm API'leri test et
python app.py

# Konfigürasyonu kontrol et
python -c "from config import validate_config; print(validate_config())"
```

## NASA API Anahtarı

- Varsayılan olarak `DEMO_KEY` kullanılır (sınırlı kullanım)
- Ücretsiz NASA API anahtarı için: https://api.nasa.gov/
- API anahtarını environment variable olarak ayarlayın: `NASA_API_KEY`

## MCP Tool Kullanımı

Bu sunucu `get_mars_weather_data` adında bir tool sağlar:

```python
# Varsayılan DEMO_KEY ile
result = await get_mars_weather_data()

# Kendi API anahtarınızla
result = await get_mars_weather_data(api_key="your_nasa_api_key")
```

## Örnek Çıktı

```json
{
  "sol": "681",
  "first_utc": "2020-10-25T22:29:51Z",
  "last_utc": "2020-10-26T23:09:26Z",
  "season": "fall",
  "northern_season": "mid winter",
  "southern_season": "mid summer",
  "temperature": {
    "average": -62.434,
    "minimum": -95.447,
    "maximum": -4.444,
    "unit": "Celsius"
  },
  "pressure": {
    "average": 743.55,
    "minimum": 718.463,
    "maximum": 760.2244,
    "unit": "Pa"
  },
  "wind_speed": {
    "average": 5.632,
    "minimum": 0.228,
    "maximum": 18.577,
    "unit": "m/s"
  },
  "wind_direction": {
    "compass_point": "WNW",
    "compass_degrees": 292.5
  }
}
```

## 📁 Proje Yapısı

```
├── nasa_apis/                    # NASA API modülleri
│   ├── __init__.py
│   ├── base.py                   # Base API client sınıfı
│   ├── apod.py                   # Astronomy Picture of the Day
│   ├── asteroids.py              # Near Earth Objects
│   ├── donki.py                  # Space Weather Database
│   ├── earth.py                  # Earth Imagery
│   ├── eonet.py                  # Natural Event Tracker
│   ├── epic.py                   # Earth Polychromatic Imaging
│   ├── exoplanet.py              # Exoplanet Archive
│   ├── mars_rover.py             # Mars Rover Photos
│   ├── mars_weather.py           # Mars Weather
│   └── nasa_library.py           # NASA Image Library
├── app.py                        # Ana uygulama ve API manager
├── server.py                     # MCP sunucu ve tool'lar
├── config.py                     # Konfigürasyon yönetimi
├── requirements.txt              # Python bağımlılıkları
├── smithery.yaml                 # MCP konfigürasyon dosyası
├── Dockerfile                    # Docker konteyner konfigürasyonu
├── .env.example                  # Environment variables örneği
├── nasa_api_endpoints.md         # API endpoint dokümantasyonu
└── README.md                     # Bu dosya
```

## Notlar

- InSight lander'ı 2022'de görevini tamamladığı için API eski verileri döndürür
- Veriler eğitim ve test amaçlı kullanım içindir
- Gerçek zamanlı Mars hava durumu verileri için NASA'nın diğer API'lerini kontrol edin
