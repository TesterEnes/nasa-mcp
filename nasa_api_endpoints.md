# NASA API Endpoints Documentation

## 1. APOD - Astronomy Picture of the Day
- **URL**: `https://api.nasa.gov/planetary/apod`
- **Parameters**: 
  - `api_key`: NASA API key
  - `date`: YYYY-MM-DD format (optional)
  - `start_date`: YYYY-MM-DD format (optional)
  - `end_date`: YYYY-MM-DD format (optional)
  - `count`: Number of images to return (optional)
  - `thumbs`: Return thumbnail URL (optional)

## 2. Asteroids NeoWs - Near Earth Object Web Service
- **URL**: `https://api.nasa.gov/neo/rest/v1/`
- **Endpoints**:
  - `/feed`: Get asteroids by date range
  - `/lookup`: Get specific asteroid by ID
  - `/browse`: Browse all asteroids
  - `/stats`: Get statistics

## 3. DONKI - Space Weather Database
- **URL**: `https://api.nasa.gov/DONKI/`
- **Endpoints**:
  - `/CME`: Coronal Mass Ejection
  - `/GST`: Geomagnetic Storm
  - `/IPS`: Interplanetary Shock
  - `/FLR`: Solar Flare
  - `/SEP`: Solar Energetic Particle
  - `/MPC`: Magnetopause Crossing
  - `/RBE`: Radiation Belt Enhancement
  - `/HSS`: High Speed Stream

## 4. Earth Imagery
- **URL**: `https://api.nasa.gov/planetary/earth/`
- **Endpoints**:
  - `/imagery`: Get Earth imagery
  - `/assets`: Get available assets

## 5. EONET - Earth Observatory Natural Event Tracker
- **URL**: `https://eonet.gsfc.nasa.gov/api/v3/`
- **Endpoints**:
  - `/events`: Get natural events
  - `/categories`: Get event categories
  - `/layers`: Get data layers
  - `/sources`: Get data sources

## 6. EPIC - Earth Polychromatic Imaging Camera
- **URL**: `https://api.nasa.gov/EPIC/api/`
- **Endpoints**:
  - `/natural`: Natural color images
  - `/enhanced`: Enhanced color images
  - `/all`: All available images

## 7. Exoplanet Archive
- **URL**: `https://exoplanetarchive.ipac.caltech.edu/TAP/sync`
- **Method**: TAP (Table Access Protocol)
- **Query**: ADQL (Astronomical Data Query Language)

## 8. Mars Rover Photos
- **URL**: `https://api.nasa.gov/mars-photos/api/v1/rovers/`
- **Rovers**: curiosity, opportunity, spirit, perseverance, ingenuity
- **Endpoints**:
  - `/photos`: Get photos by sol/earth date
  - `/latest_photos`: Get latest photos
  - `/manifests`: Get mission manifest

## 9. NASA Image and Video Library
- **URL**: `https://images-api.nasa.gov/`
- **Endpoints**:
  - `/search`: Search media
  - `/asset/{nasa_id}`: Get asset details
  - `/metadata/{nasa_id}`: Get metadata
  - `/captions/{nasa_id}`: Get captions

## 10. InSight Mars Weather
- **URL**: `https://api.nasa.gov/insight_weather/`
- **Parameters**: 
  - `api_key`: NASA API key
  - `feedtype`: json
  - `ver`: 1.0

## 11. TechTransfer
- **URL**: `https://api.nasa.gov/techtransfer/`
- **Endpoints**:
  - `/patent`: Patents
  - `/software`: Software
  - `/spinoff`: Spinoffs

## 12. Satellite Situation Center
- **URL**: `https://sscweb.gsfc.nasa.gov/WS/`
- **SOAP/REST**: Spacecraft location data

## 13. SSD/CNEOS - Solar System Dynamics
- **URL**: `https://ssd-api.jpl.nasa.gov/`
- **Endpoints**:
  - `/cad.api`: Close Approach Data
  - `/fireball.api`: Fireball data
  - `/sentry.api`: Sentry risk table

## 14. Techport
- **URL**: `https://api.nasa.gov/techport/api/`
- **Endpoints**:
  - `/projects`: Get projects
  - `/projects/{id}`: Get specific project

## 15. TLE API - Two Line Element
- **URL**: `https://tle.ivanstanojevic.me/api/tle/`
- **Parameters**: Satellite NORAD ID or name

## 16. Vesta/Moon/Mars Trek WMTS
- **URL**: Various WMTS endpoints for planetary imagery
- **Format**: Web Map Tile Service
