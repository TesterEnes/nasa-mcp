"""
Extended MCP Tools for NASA APIs
This file contains additional tools that can be imported into the main server
"""

from app import NASAAPIManager
from typing import Optional

# Initialize NASA API Manager
nasa_manager = NASAAPIManager()

# EPIC Tools
async def get_epic_natural_images(api_key: str = "DEMO_KEY", date: Optional[str] = None) -> dict:
    """Get natural color Earth images from EPIC"""
    api = nasa_manager.epic if api_key == nasa_manager.api_key else nasa_manager.epic.__class__(api_key)
    return api.get_natural_images(date)

async def get_epic_enhanced_images(api_key: str = "DEMO_KEY", date: Optional[str] = None) -> dict:
    """Get enhanced color Earth images from EPIC"""
    api = nasa_manager.epic if api_key == nasa_manager.api_key else nasa_manager.epic.__class__(api_key)
    return api.get_enhanced_images(date)

# EONET Tools
async def get_natural_events(status: Optional[str] = None, limit: Optional[int] = None, 
                           days: Optional[int] = None, category: Optional[str] = None) -> dict:
    """Get natural events from EONET"""
    return nasa_manager.eonet.get_events(status, limit, days, category)

async def get_event_categories() -> dict:
    """Get all natural event categories"""
    return nasa_manager.eonet.get_categories()

# DONKI Tools
async def get_coronal_mass_ejections(api_key: str = "DEMO_KEY", start_date: Optional[str] = None, 
                                   end_date: Optional[str] = None) -> dict:
    """Get Coronal Mass Ejection events"""
    api = nasa_manager.donki if api_key == nasa_manager.api_key else nasa_manager.donki.__class__(api_key)
    return api.get_coronal_mass_ejections(start_date, end_date)

async def get_solar_flares(api_key: str = "DEMO_KEY", start_date: Optional[str] = None, 
                          end_date: Optional[str] = None) -> dict:
    """Get Solar Flare events"""
    api = nasa_manager.donki if api_key == nasa_manager.api_key else nasa_manager.donki.__class__(api_key)
    return api.get_solar_flares(start_date, end_date)

async def get_geomagnetic_storms(api_key: str = "DEMO_KEY", start_date: Optional[str] = None, 
                               end_date: Optional[str] = None) -> dict:
    """Get Geomagnetic Storm events"""
    api = nasa_manager.donki if api_key == nasa_manager.api_key else nasa_manager.donki.__class__(api_key)
    return api.get_geomagnetic_storms(start_date, end_date)

# NASA Library Tools
async def search_nasa_media(q: str, media_type: Optional[str] = None, year_start: Optional[str] = None,
                           year_end: Optional[str] = None, page: int = 1, page_size: int = 100) -> dict:
    """Search NASA media library"""
    return nasa_manager.nasa_library.search(q, media_type=media_type, year_start=year_start, 
                                           year_end=year_end, page=page, page_size=page_size)

async def get_nasa_asset(nasa_id: str) -> dict:
    """Get NASA media asset details"""
    return nasa_manager.nasa_library.get_asset(nasa_id)

# Exoplanet Tools
async def get_confirmed_exoplanets(limit: int = 100) -> dict:
    """Get confirmed exoplanets"""
    return nasa_manager.exoplanet.get_confirmed_planets(limit)

async def search_exoplanets_by_name(planet_name: str) -> dict:
    """Search exoplanets by name"""
    return nasa_manager.exoplanet.search_planets_by_name(planet_name)

async def get_habitable_exoplanets(limit: int = 50) -> dict:
    """Get potentially habitable exoplanets"""
    return nasa_manager.exoplanet.get_habitable_zone_planets(limit)

async def get_recent_exoplanet_discoveries(years_back: int = 5, limit: int = 100) -> dict:
    """Get recently discovered exoplanets"""
    return nasa_manager.exoplanet.get_recent_discoveries(years_back, limit)
