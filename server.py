from mcp.server.fastmcp import FastMCP
from app import NASAAPIManager
from typing import Optional

# Initialize MCP server
mcp = FastMCP("nasa-apis-mcp")

# Initialize NASA API Manager
nasa_manager = NASAAPIManager()

# APOD Tools
@mcp.tool()
async def get_astronomy_picture_of_the_day(api_key: str = "DEMO_KEY", date: Optional[str] = None, hd: bool = True) -> dict:
    """
    Get NASA's Astronomy Picture of the Day.

    Args:
        api_key: NASA API key
        date: Date in YYYY-MM-DD format (optional, defaults to today)
        hd: Return HD version if available

    Returns:
        Dictionary containing APOD data including title, explanation, image URL, etc.
    """
    api = nasa_manager.apod if api_key == nasa_manager.api_key else nasa_manager.apod.__class__(api_key)
    return api.get_picture_of_the_day(date, hd)

@mcp.tool()
async def get_apod_date_range(api_key: str = "DEMO_KEY", start_date: str = "", end_date: str = "") -> dict:
    """
    Get APOD pictures for a date range.

    Args:
        api_key: NASA API key
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format

    Returns:
        List of APOD data for the specified date range
    """
    api = nasa_manager.apod if api_key == nasa_manager.api_key else nasa_manager.apod.__class__(api_key)
    return api.get_pictures_by_date_range(start_date, end_date)

@mcp.tool()
async def get_random_apod(api_key: str = "DEMO_KEY", count: int = 1) -> dict:
    """
    Get random APOD pictures.

    Args:
        api_key: NASA API key
        count: Number of random pictures (max 100)

    Returns:
        List of random APOD data
    """
    api = nasa_manager.apod if api_key == nasa_manager.api_key else nasa_manager.apod.__class__(api_key)
    return api.get_random_pictures(count)

# Asteroids Tools
@mcp.tool()
async def get_asteroid_feed(api_key: str = "DEMO_KEY", start_date: Optional[str] = None, end_date: Optional[str] = None) -> dict:
    """
    Get asteroids approaching Earth within date range.

    Args:
        api_key: NASA API key
        start_date: Start date in YYYY-MM-DD format (optional)
        end_date: End date in YYYY-MM-DD format (optional)

    Returns:
        Dictionary containing asteroid feed data
    """
    api = nasa_manager.asteroids if api_key == nasa_manager.api_key else nasa_manager.asteroids.__class__(api_key)
    return api.get_feed(start_date, end_date)

@mcp.tool()
async def get_asteroid_by_id(api_key: str = "DEMO_KEY", asteroid_id: str = "") -> dict:
    """
    Get specific asteroid details by ID.

    Args:
        api_key: NASA API key
        asteroid_id: NASA JPL asteroid database ID

    Returns:
        Dictionary containing detailed asteroid information
    """
    api = nasa_manager.asteroids if api_key == nasa_manager.api_key else nasa_manager.asteroids.__class__(api_key)
    return api.get_asteroid_by_id(asteroid_id)

@mcp.tool()
async def browse_asteroids(api_key: str = "DEMO_KEY", page: int = 0, size: int = 20) -> dict:
    """
    Browse all asteroids in NASA database.

    Args:
        api_key: NASA API key
        page: Page number (0-based)
        size: Number of asteroids per page (max 100)

    Returns:
        Dictionary containing paginated asteroid data
    """
    api = nasa_manager.asteroids if api_key == nasa_manager.api_key else nasa_manager.asteroids.__class__(api_key)
    return api.browse_asteroids(page, size)

@mcp.tool()
async def get_asteroid_statistics(api_key: str = "DEMO_KEY") -> dict:
    """
    Get Near Earth Object statistics.

    Args:
        api_key: NASA API key

    Returns:
        Dictionary containing NEO statistics
    """
    api = nasa_manager.asteroids if api_key == nasa_manager.api_key else nasa_manager.asteroids.__class__(api_key)
    return api.get_statistics()

# Mars Weather Tool
@mcp.tool()
async def get_mars_weather_data(api_key: str = "DEMO_KEY") -> dict:
    """
    Get the latest Mars weather data from NASA InSight Weather API.

    Args:
        api_key: NASA API key

    Returns:
        Dictionary containing Mars weather information including temperature, pressure, wind data
    """
    api = nasa_manager.mars_weather if api_key == nasa_manager.api_key else nasa_manager.mars_weather.__class__(api_key)
    return api.get_weather()

# Mars Rover Tools
@mcp.tool()
async def get_mars_rover_photos_by_sol(api_key: str = "DEMO_KEY", rover: str = "curiosity",
                                      sol: int = 1000, camera: Optional[str] = None, page: int = 1) -> dict:
    """
    Get Mars rover photos by Martian sol (day).

    Args:
        api_key: NASA API key
        rover: Rover name (curiosity, opportunity, spirit, perseverance)
        sol: Martian sol number
        camera: Camera name (optional)
        page: Page number for pagination

    Returns:
        Dictionary containing rover photos
    """
    api = nasa_manager.mars_rover if api_key == nasa_manager.api_key else nasa_manager.mars_rover.__class__(api_key)
    return api.get_photos_by_sol(rover, sol, camera, page)

@mcp.tool()
async def get_mars_rover_photos_by_date(api_key: str = "DEMO_KEY", rover: str = "curiosity",
                                       earth_date: str = "2023-01-01", camera: Optional[str] = None, page: int = 1) -> dict:
    """
    Get Mars rover photos by Earth date.

    Args:
        api_key: NASA API key
        rover: Rover name
        earth_date: Earth date in YYYY-MM-DD format
        camera: Camera name (optional)
        page: Page number for pagination

    Returns:
        Dictionary containing rover photos
    """
    api = nasa_manager.mars_rover if api_key == nasa_manager.api_key else nasa_manager.mars_rover.__class__(api_key)
    return api.get_photos_by_earth_date(rover, earth_date, camera, page)

@mcp.tool()
async def get_mars_rover_latest_photos(api_key: str = "DEMO_KEY", rover: str = "curiosity") -> dict:
    """
    Get latest photos from Mars rover.

    Args:
        api_key: NASA API key
        rover: Rover name

    Returns:
        Dictionary containing latest rover photos
    """
    api = nasa_manager.mars_rover if api_key == nasa_manager.api_key else nasa_manager.mars_rover.__class__(api_key)
    return api.get_latest_photos(rover)

@mcp.tool()
async def get_mars_rover_manifest(api_key: str = "DEMO_KEY", rover: str = "curiosity") -> dict:
    """
    Get Mars rover mission manifest.

    Args:
        api_key: NASA API key
        rover: Rover name

    Returns:
        Dictionary containing rover mission manifest
    """
    api = nasa_manager.mars_rover if api_key == nasa_manager.api_key else nasa_manager.mars_rover.__class__(api_key)
    return api.get_manifest(rover)

# Earth Imagery Tools
@mcp.tool()
async def get_earth_imagery(api_key: str = "DEMO_KEY", lat: float = 29.78, lon: float = -95.33,
                           date: Optional[str] = None, dim: float = 0.15, cloud_score: bool = False) -> dict:
    """
    Get Earth imagery for specific coordinates.

    Args:
        api_key: NASA API key
        lat: Latitude (-90 to 90)
        lon: Longitude (-180 to 180)
        date: Date in YYYY-MM-DD format (optional)
        dim: Image dimension in degrees (0.025 to 0.25)
        cloud_score: Calculate cloud score

    Returns:
        Dictionary containing Earth imagery data
    """
    api = nasa_manager.earth if api_key == nasa_manager.api_key else nasa_manager.earth.__class__(api_key)
    return api.get_imagery(lat, lon, date, dim, cloud_score)

@mcp.tool()
async def get_earth_assets(api_key: str = "DEMO_KEY", lat: float = 29.78, lon: float = -95.33,
                          date: Optional[str] = None, dim: float = 0.15) -> dict:
    """
    Get available Earth imagery assets for coordinates.

    Args:
        api_key: NASA API key
        lat: Latitude
        lon: Longitude
        date: Date in YYYY-MM-DD format (optional)
        dim: Search area dimension in degrees

    Returns:
        Dictionary containing available assets
    """
    api = nasa_manager.earth if api_key == nasa_manager.api_key else nasa_manager.earth.__class__(api_key)
    return api.get_assets(lat, lon, date, dim)

# EPIC Tools
@mcp.tool()
async def get_epic_natural_images(api_key: str = "DEMO_KEY", date: Optional[str] = None) -> dict:
    """
    Get natural color Earth images from EPIC.

    Args:
        api_key: NASA API key
        date: Date in YYYY-MM-DD format (optional)

    Returns:
        Dictionary containing natural color Earth images
    """
    api = nasa_manager.epic if api_key == nasa_manager.api_key else nasa_manager.epic.__class__(api_key)
    return api.get_natural_images(date)

@mcp.tool()
async def get_epic_enhanced_images(api_key: str = "DEMO_KEY", date: Optional[str] = None) -> dict:
    """
    Get enhanced color Earth images from EPIC.

    Args:
        api_key: NASA API key
        date: Date in YYYY-MM-DD format (optional)

    Returns:
        Dictionary containing enhanced color Earth images
    """
    api = nasa_manager.epic if api_key == nasa_manager.api_key else nasa_manager.epic.__class__(api_key)
    return api.get_enhanced_images(date)

# EONET Tools
@mcp.tool()
async def get_natural_events(status: Optional[str] = None, limit: Optional[int] = None,
                           days: Optional[int] = None, category: Optional[str] = None) -> dict:
    """
    Get natural events from EONET.

    Args:
        status: Event status ('open' or 'closed')
        limit: Limit number of events
        days: Get events from last N days
        category: Event category ID

    Returns:
        Dictionary containing natural events
    """
    return nasa_manager.eonet.get_events(status, limit, days, category)

@mcp.tool()
async def get_event_categories() -> dict:
    """
    Get all natural event categories from EONET.

    Returns:
        Dictionary containing event categories
    """
    return nasa_manager.eonet.get_categories()

# DONKI Tools
@mcp.tool()
async def get_solar_flares(api_key: str = "DEMO_KEY", start_date: Optional[str] = None,
                          end_date: Optional[str] = None) -> dict:
    """
    Get Solar Flare events from DONKI.

    Args:
        api_key: NASA API key
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format

    Returns:
        Dictionary containing solar flare events
    """
    api = nasa_manager.donki if api_key == nasa_manager.api_key else nasa_manager.donki.__class__(api_key)
    return api.get_solar_flares(start_date, end_date)

@mcp.tool()
async def get_coronal_mass_ejections(api_key: str = "DEMO_KEY", start_date: Optional[str] = None,
                                   end_date: Optional[str] = None) -> dict:
    """
    Get Coronal Mass Ejection events from DONKI.

    Args:
        api_key: NASA API key
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format

    Returns:
        Dictionary containing CME events
    """
    api = nasa_manager.donki if api_key == nasa_manager.api_key else nasa_manager.donki.__class__(api_key)
    return api.get_coronal_mass_ejections(start_date, end_date)

# NASA Library Tools
@mcp.tool()
async def search_nasa_media(q: str, media_type: Optional[str] = None, year_start: Optional[str] = None,
                           year_end: Optional[str] = None, page: int = 1, page_size: int = 100) -> dict:
    """
    Search NASA media library.

    Args:
        q: Search query
        media_type: Media type (image, video, audio)
        year_start: Start year (YYYY)
        year_end: End year (YYYY)
        page: Page number
        page_size: Items per page (max 100)

    Returns:
        Dictionary containing search results
    """
    return nasa_manager.nasa_library.search(q, media_type=media_type, year_start=year_start,
                                           year_end=year_end, page=page, page_size=page_size)

# Exoplanet Tools
@mcp.tool()
async def get_confirmed_exoplanets(limit: int = 100) -> dict:
    """
    Get confirmed exoplanets.

    Args:
        limit: Maximum number of results

    Returns:
        Dictionary containing confirmed exoplanet data
    """
    return nasa_manager.exoplanet.get_confirmed_planets(limit)

@mcp.tool()
async def search_exoplanets_by_name(planet_name: str) -> dict:
    """
    Search exoplanets by name.

    Args:
        planet_name: Planet name to search for

    Returns:
        Dictionary containing matching exoplanets
    """
    return nasa_manager.exoplanet.search_planets_by_name(planet_name)

@mcp.tool()
async def get_habitable_exoplanets(limit: int = 50) -> dict:
    """
    Get potentially habitable exoplanets.

    Args:
        limit: Maximum number of results

    Returns:
        Dictionary containing potentially habitable exoplanets
    """
    return nasa_manager.exoplanet.get_habitable_zone_planets(limit)

if __name__ == "__main__":
    mcp.run(transport="stdio")