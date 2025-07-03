"""
Earth Imagery API
"""
from .base import NASAAPIBase
from typing import Dict, Any, Optional


class EarthAPI(NASAAPIBase):
    """NASA Earth Imagery API client"""
    
    def __init__(self, api_key: str = "DEMO_KEY"):
        super().__init__(api_key)
        self.base_endpoint = f"{self.base_url}/planetary/earth"
    
    def get_imagery(self, lat: float, lon: float, date: Optional[str] = None, 
                   dim: float = 0.15, cloud_score: bool = False) -> Dict[str, Any]:
        """
        Get Earth imagery for specific coordinates
        
        Args:
            lat: Latitude
            lon: Longitude  
            date: Date in YYYY-MM-DD format (optional, defaults to most recent)
            dim: Width and height of image in degrees (0.025 to 0.25)
            cloud_score: Calculate cloud score for image
            
        Returns:
            Dictionary containing Earth imagery data
        """
        if not (-90 <= lat <= 90):
            return {"error": "Latitude must be between -90 and 90"}
        if not (-180 <= lon <= 180):
            return {"error": "Longitude must be between -180 and 180"}
        if not (0.025 <= dim <= 0.25):
            return {"error": "Dimension must be between 0.025 and 0.25"}
        
        params = {
            "lat": lat,
            "lon": lon,
            "dim": dim
        }
        
        if date:
            try:
                date = self._format_date(date)
                params["date"] = date
            except ValueError as e:
                return {"error": str(e)}
        
        if cloud_score:
            params["cloud_score"] = "true"
        
        endpoint = f"{self.base_endpoint}/imagery"
        return self._make_request(endpoint, params)
    
    def get_assets(self, lat: float, lon: float, date: Optional[str] = None, 
                  dim: float = 0.15) -> Dict[str, Any]:
        """
        Get available Earth imagery assets for specific coordinates
        
        Args:
            lat: Latitude
            lon: Longitude
            date: Date in YYYY-MM-DD format (optional)
            dim: Width and height of search area in degrees
            
        Returns:
            Dictionary containing available assets
        """
        if not (-90 <= lat <= 90):
            return {"error": "Latitude must be between -90 and 90"}
        if not (-180 <= lon <= 180):
            return {"error": "Longitude must be between -180 and 180"}
        if not (0.025 <= dim <= 0.25):
            return {"error": "Dimension must be between 0.025 and 0.25"}
        
        params = {
            "lat": lat,
            "lon": lon,
            "dim": dim
        }
        
        if date:
            try:
                date = self._format_date(date)
                params["date"] = date
            except ValueError as e:
                return {"error": str(e)}
        
        endpoint = f"{self.base_endpoint}/assets"
        return self._make_request(endpoint, params)
