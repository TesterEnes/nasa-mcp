"""
NASA Image and Video Library API
"""
from .base import NASAAPIBase
from typing import Dict, Any, Optional


class NASALibraryAPI(NASAAPIBase):
    """NASA Image and Video Library API client"""
    
    def __init__(self, api_key: str = "DEMO_KEY"):
        super().__init__(api_key)
        # NASA Library API doesn't require API key
        self.base_endpoint = "https://images-api.nasa.gov"
    
    def search(self, q: str, center: Optional[str] = None, description: Optional[str] = None,
              keywords: Optional[str] = None, location: Optional[str] = None,
              media_type: Optional[str] = None, nasa_id: Optional[str] = None,
              photographer: Optional[str] = None, secondary_creator: Optional[str] = None,
              title: Optional[str] = None, year_start: Optional[str] = None,
              year_end: Optional[str] = None, page: int = 1, page_size: int = 100) -> Dict[str, Any]:
        """
        Search NASA media library
        
        Args:
            q: Search query
            center: NASA center
            description: Description search
            keywords: Keywords search
            location: Location search
            media_type: Media type (image, video, audio)
            nasa_id: NASA ID
            photographer: Photographer name
            secondary_creator: Secondary creator
            title: Title search
            year_start: Start year (YYYY)
            year_end: End year (YYYY)
            page: Page number
            page_size: Items per page (max 100)
            
        Returns:
            Dictionary containing search results
        """
        params = {
            'q': q,
            'page': page,
            'page_size': min(page_size, 100)
        }
        
        # Add optional parameters
        optional_params = {
            'center': center,
            'description': description,
            'keywords': keywords,
            'location': location,
            'media_type': media_type,
            'nasa_id': nasa_id,
            'photographer': photographer,
            'secondary_creator': secondary_creator,
            'title': title,
            'year_start': year_start,
            'year_end': year_end
        }
        
        for key, value in optional_params.items():
            if value:
                params[key] = value
        
        endpoint = f"{self.base_endpoint}/search"
        return self._make_external_request(endpoint, params)
    
    def get_asset(self, nasa_id: str) -> Dict[str, Any]:
        """
        Get asset details by NASA ID
        
        Args:
            nasa_id: NASA asset ID
            
        Returns:
            Dictionary containing asset details
        """
        endpoint = f"{self.base_endpoint}/asset/{nasa_id}"
        return self._make_external_request(endpoint)
    
    def get_metadata(self, nasa_id: str) -> Dict[str, Any]:
        """
        Get metadata by NASA ID
        
        Args:
            nasa_id: NASA asset ID
            
        Returns:
            Dictionary containing metadata
        """
        endpoint = f"{self.base_endpoint}/metadata/{nasa_id}"
        return self._make_external_request(endpoint)
    
    def get_captions(self, nasa_id: str) -> Dict[str, Any]:
        """
        Get captions by NASA ID
        
        Args:
            nasa_id: NASA asset ID
            
        Returns:
            Dictionary containing captions
        """
        endpoint = f"{self.base_endpoint}/captions/{nasa_id}"
        return self._make_external_request(endpoint)
