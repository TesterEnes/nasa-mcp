"""
APOD - Astronomy Picture of the Day API
"""
from .base import NASAAPIBase
from typing import Dict, Any, Optional, List
from datetime import datetime


class APODAPI(NASAAPIBase):
    """NASA Astronomy Picture of the Day API client"""
    
    def __init__(self, api_key: str = "DEMO_KEY"):
        super().__init__(api_key)
        self.endpoint = f"{self.base_url}/planetary/apod"
    
    def get_picture_of_the_day(self, date: Optional[str] = None, hd: bool = True) -> Dict[str, Any]:
        """
        Get Astronomy Picture of the Day
        
        Args:
            date: Date in YYYY-MM-DD format (optional, defaults to today)
            hd: Return HD version if available
            
        Returns:
            Dictionary containing APOD data
        """
        params = {}
        if date:
            params['date'] = date
        if hd:
            params['hd'] = 'true'
            
        return self._make_request(self.endpoint, params)
    
    def get_pictures_by_date_range(self, start_date: str, end_date: str) -> Dict[str, Any]:
        """
        Get APOD pictures for a date range
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            
        Returns:
            List of APOD data
        """
        params = {
            'start_date': start_date,
            'end_date': end_date
        }
        
        return self._make_request(self.endpoint, params)
    
    def get_random_pictures(self, count: int = 1) -> Dict[str, Any]:
        """
        Get random APOD pictures
        
        Args:
            count: Number of random pictures to return (max 100)
            
        Returns:
            List of random APOD data
        """
        params = {
            'count': min(count, 100)  # API limit
        }
        
        return self._make_request(self.endpoint, params)
