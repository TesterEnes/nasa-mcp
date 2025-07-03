"""
EONET - Earth Observatory Natural Event Tracker API
"""
from .base import NASAAPIBase
from typing import Dict, Any, Optional, List


class EONETAPI(NASAAPIBase):
    """NASA EONET (Earth Observatory Natural Event Tracker) API client"""
    
    def __init__(self, api_key: str = "DEMO_KEY"):
        super().__init__(api_key)
        # EONET API doesn't require API key and uses different base URL
        self.base_endpoint = "https://eonet.gsfc.nasa.gov/api/v3"
    
    def get_events(self, status: Optional[str] = None, limit: Optional[int] = None, 
                  days: Optional[int] = None, category: Optional[str] = None,
                  source: Optional[str] = None, bbox: Optional[str] = None) -> Dict[str, Any]:
        """
        Get natural events from EONET
        
        Args:
            status: Event status ('open' or 'closed')
            limit: Limit number of events returned
            days: Get events from last N days
            category: Event category ID
            source: Data source ID
            bbox: Bounding box coordinates (minX,minY,maxX,maxY)
            
        Returns:
            Dictionary containing natural events data
        """
        params = {}
        
        if status and status.lower() in ['open', 'closed']:
            params['status'] = status.lower()
        if limit and isinstance(limit, int) and limit > 0:
            params['limit'] = limit
        if days and isinstance(days, int) and days > 0:
            params['days'] = days
        if category:
            params['category'] = category
        if source:
            params['source'] = source
        if bbox:
            params['bbox'] = bbox
        
        endpoint = f"{self.base_endpoint}/events"
        return self._make_external_request(endpoint, params)
    
    def get_event_by_id(self, event_id: str) -> Dict[str, Any]:
        """
        Get specific event by ID
        
        Args:
            event_id: EONET event ID
            
        Returns:
            Dictionary containing event details
        """
        endpoint = f"{self.base_endpoint}/events/{event_id}"
        return self._make_external_request(endpoint)
    
    def get_categories(self) -> Dict[str, Any]:
        """
        Get all event categories
        
        Returns:
            Dictionary containing event categories
        """
        endpoint = f"{self.base_endpoint}/categories"
        return self._make_external_request(endpoint)
    
    def get_category_by_id(self, category_id: str, status: Optional[str] = None, 
                          limit: Optional[int] = None, days: Optional[int] = None) -> Dict[str, Any]:
        """
        Get events by category
        
        Args:
            category_id: Category ID
            status: Event status ('open' or 'closed')
            limit: Limit number of events returned
            days: Get events from last N days
            
        Returns:
            Dictionary containing events for specific category
        """
        params = {}
        
        if status and status.lower() in ['open', 'closed']:
            params['status'] = status.lower()
        if limit and isinstance(limit, int) and limit > 0:
            params['limit'] = limit
        if days and isinstance(days, int) and days > 0:
            params['days'] = days
        
        endpoint = f"{self.base_endpoint}/categories/{category_id}"
        return self._make_external_request(endpoint, params)
    
    def get_sources(self) -> Dict[str, Any]:
        """
        Get all data sources
        
        Returns:
            Dictionary containing data sources
        """
        endpoint = f"{self.base_endpoint}/sources"
        return self._make_external_request(endpoint)
    
    def get_layers(self, category: Optional[str] = None) -> Dict[str, Any]:
        """
        Get available data layers
        
        Args:
            category: Filter by category ID
            
        Returns:
            Dictionary containing data layers
        """
        params = {}
        if category:
            params['category'] = category
        
        endpoint = f"{self.base_endpoint}/layers"
        return self._make_external_request(endpoint, params)
