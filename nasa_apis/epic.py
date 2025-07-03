"""
EPIC - Earth Polychromatic Imaging Camera API
"""
from .base import NASAAPIBase
from typing import Dict, Any, Optional


class EPICAPI(NASAAPIBase):
    """NASA EPIC (Earth Polychromatic Imaging Camera) API client"""
    
    def __init__(self, api_key: str = "DEMO_KEY"):
        super().__init__(api_key)
        self.base_endpoint = f"{self.base_url}/EPIC/api"
    
    def get_natural_images(self, date: Optional[str] = None) -> Dict[str, Any]:
        """
        Get natural color Earth images from EPIC
        
        Args:
            date: Date in YYYY-MM-DD format (optional, defaults to most recent available)
            
        Returns:
            Dictionary containing natural color image data
        """
        endpoint = f"{self.base_endpoint}/natural"
        
        if date:
            try:
                date = self._format_date(date)
                endpoint += f"/date/{date}"
            except ValueError as e:
                return {"error": str(e)}
        
        return self._make_request(endpoint)
    
    def get_enhanced_images(self, date: Optional[str] = None) -> Dict[str, Any]:
        """
        Get enhanced color Earth images from EPIC
        
        Args:
            date: Date in YYYY-MM-DD format (optional, defaults to most recent available)
            
        Returns:
            Dictionary containing enhanced color image data
        """
        endpoint = f"{self.base_endpoint}/enhanced"
        
        if date:
            try:
                date = self._format_date(date)
                endpoint += f"/date/{date}"
            except ValueError as e:
                return {"error": str(e)}
        
        return self._make_request(endpoint)
    
    def get_all_natural_dates(self) -> Dict[str, Any]:
        """
        Get all available dates for natural color images
        
        Returns:
            List of available dates
        """
        endpoint = f"{self.base_endpoint}/natural/all"
        return self._make_request(endpoint)
    
    def get_all_enhanced_dates(self) -> Dict[str, Any]:
        """
        Get all available dates for enhanced color images
        
        Returns:
            List of available dates
        """
        endpoint = f"{self.base_endpoint}/enhanced/all"
        return self._make_request(endpoint)
    
    def get_natural_image_url(self, image_name: str, date: str) -> str:
        """
        Get direct URL for natural color image
        
        Args:
            image_name: Image filename from API response
            date: Date in YYYY-MM-DD format
            
        Returns:
            Direct URL to image
        """
        date_formatted = date.replace('-', '/')
        return f"https://api.nasa.gov/EPIC/archive/natural/{date_formatted}/png/{image_name}.png?api_key={self.api_key}"
    
    def get_enhanced_image_url(self, image_name: str, date: str) -> str:
        """
        Get direct URL for enhanced color image
        
        Args:
            image_name: Image filename from API response
            date: Date in YYYY-MM-DD format
            
        Returns:
            Direct URL to image
        """
        date_formatted = date.replace('-', '/')
        return f"https://api.nasa.gov/EPIC/archive/enhanced/{date_formatted}/png/{image_name}.png?api_key={self.api_key}"
