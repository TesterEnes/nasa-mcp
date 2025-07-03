"""
Asteroids NeoWs - Near Earth Object Web Service API
"""
from .base import NASAAPIBase
from typing import Dict, Any, Optional
from datetime import datetime, timedelta


class AsteroidsAPI(NASAAPIBase):
    """NASA Near Earth Object Web Service API client"""
    
    def __init__(self, api_key: str = "DEMO_KEY"):
        super().__init__(api_key)
        self.base_endpoint = f"{self.base_url}/neo/rest/v1"
    
    def get_feed(self, start_date: Optional[str] = None, end_date: Optional[str] = None) -> Dict[str, Any]:
        """
        Get asteroids approaching Earth within date range
        
        Args:
            start_date: Start date in YYYY-MM-DD format (optional, defaults to today)
            end_date: End date in YYYY-MM-DD format (optional, defaults to 7 days from start)
            
        Returns:
            Dictionary containing asteroid feed data
        """
        params = {}
        
        if start_date:
            params['start_date'] = start_date
        if end_date:
            params['end_date'] = end_date
            
        endpoint = f"{self.base_endpoint}/feed"
        return self._make_request(endpoint, params)
    
    def get_asteroid_by_id(self, asteroid_id: str) -> Dict[str, Any]:
        """
        Get specific asteroid by ID
        
        Args:
            asteroid_id: NASA JPL asteroid database ID
            
        Returns:
            Dictionary containing asteroid details
        """
        endpoint = f"{self.base_endpoint}/neo/{asteroid_id}"
        return self._make_request(endpoint)
    
    def browse_asteroids(self, page: int = 0, size: int = 20) -> Dict[str, Any]:
        """
        Browse all asteroids in database
        
        Args:
            page: Page number (0-based)
            size: Number of asteroids per page (max 100)
            
        Returns:
            Dictionary containing paginated asteroid data
        """
        params = {
            'page': page,
            'size': min(size, 100)  # API limit
        }
        
        endpoint = f"{self.base_endpoint}/neo/browse"
        return self._make_request(endpoint, params)
    
    def get_statistics(self) -> Dict[str, Any]:
        """
        Get Near Earth Object statistics
        
        Returns:
            Dictionary containing NEO statistics
        """
        endpoint = f"{self.base_endpoint}/stats"
        return self._make_request(endpoint)
