# NASA Mars Weather MCP Server

Bu proje, NASA InSight Weather API'sini kullanarak Mars'taki hava durumu verilerini MCP (Model Context Protocol) üzerinden sağlayan bir sunucudur.

## Özellikler

- Mars'taki güncel hava durumu verilerini alır
- Sıcaklık, basınç, rüzgar hızı ve yönü bilgilerini sağlar
- Martian günleri (Sol) ve mevsim bilgilerini içerir
- MCP protokolü üzerinden AI modelleri tarafından kullanılabilir

## API Verileri

NASA InSight Weather API'sinden alınan veriler:
- **Sol**: Mars günü numarası
- **Sıcaklık**: Minimum, maksimum ve ortalama sıcaklık (Celsius)
- **Basınç**: Atmosferik basınç verileri (Pascal)
- **Rüzgar Hızı**: Minimum, maksimum ve ortalama rüzgar hızı (m/s)
- **Rüzgar Yönü**: Pusula yönü ve derece bilgisi
- **Mevsim**: Mars'taki mevsim bilgileri
- **Zaman**: Veri toplama periyodunun UTC zaman damgaları

## Kurulum

### Gereksinimler
```bash
pip install -r requirements.txt
```

### Doğrudan Çalıştırma
```bash
python server.py
```

### Docker ile Çalıştırma
```bash
# Docker image oluştur
docker build -t nasa-mars-weather-mcp .

# Konteyner çalıştır
docker run nasa-mars-weather-mcp

# Kendi API anahtarınızla çalıştır
docker run -e NASA_API_KEY=your_api_key_here nasa-mars-weather-mcp
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

## Dosya Yapısı

```
├── app.py              # Ana Mars hava durumu API fonksiyonu
├── server.py           # MCP sunucu konfigürasyonu
├── requirements.txt    # Python bağımlılıkları
├── smithery.yaml       # MCP konfigürasyon dosyası
├── Dockerfile         # Docker konteyner konfigürasyonu
└── README.md          # Bu dosya
```

## Notlar

- InSight lander'ı 2022'de görevini tamamladığı için API eski verileri döndürür
- Veriler eğitim ve test amaçlı kullanım içindir
- Gerçek zamanlı Mars hava durumu verileri için NASA'nın diğer API'lerini kontrol edin
