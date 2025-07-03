"""
DONKI - Space Weather Database API
"""
from .base import NASAAPIBase
from typing import Dict, Any, Optional
from datetime import datetime, timedelta


class DONKIAPI(NASAAPIBase):
    """NASA DONKI (Space Weather Database) API client"""
    
    def __init__(self, api_key: str = "DEMO_KEY"):
        super().__init__(api_key)
        self.base_endpoint = f"{self.base_url}/DONKI"
    
    def get_coronal_mass_ejections(self, start_date: Optional[str] = None, 
                                  end_date: Optional[str] = None) -> Dict[str, Any]:
        """
        Get Coronal Mass Ejection (CME) events
        
        Args:
            start_date: Start date in YYYY-MM-DD format (defaults to 30 days ago)
            end_date: End date in YYYY-MM-DD format (defaults to today)
            
        Returns:
            Dictionary containing CME events
        """
        params = self._get_date_params(start_date, end_date)
        endpoint = f"{self.base_endpoint}/CME"
        return self._make_request(endpoint, params)
    
    def get_geomagnetic_storms(self, start_date: Optional[str] = None, 
                              end_date: Optional[str] = None) -> Dict[str, Any]:
        """
        Get Geomagnetic Storm (GST) events
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            
        Returns:
            Dictionary containing GST events
        """
        params = self._get_date_params(start_date, end_date)
        endpoint = f"{self.base_endpoint}/GST"
        return self._make_request(endpoint, params)
    
    def get_interplanetary_shocks(self, start_date: Optional[str] = None, 
                                 end_date: Optional[str] = None) -> Dict[str, Any]:
        """
        Get Interplanetary Shock (IPS) events
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            
        Returns:
            Dictionary containing IPS events
        """
        params = self._get_date_params(start_date, end_date)
        endpoint = f"{self.base_endpoint}/IPS"
        return self._make_request(endpoint, params)
    
    def get_solar_flares(self, start_date: Optional[str] = None, 
                        end_date: Optional[str] = None) -> Dict[str, Any]:
        """
        Get Solar Flare (FLR) events
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            
        Returns:
            Dictionary containing FLR events
        """
        params = self._get_date_params(start_date, end_date)
        endpoint = f"{self.base_endpoint}/FLR"
        return self._make_request(endpoint, params)
    
    def get_solar_energetic_particles(self, start_date: Optional[str] = None, 
                                     end_date: Optional[str] = None) -> Dict[str, Any]:
        """
        Get Solar Energetic Particle (SEP) events
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            
        Returns:
            Dictionary containing SEP events
        """
        params = self._get_date_params(start_date, end_date)
        endpoint = f"{self.base_endpoint}/SEP"
        return self._make_request(endpoint, params)
    
    def get_magnetopause_crossings(self, start_date: Optional[str] = None, 
                                  end_date: Optional[str] = None) -> Dict[str, Any]:
        """
        Get Magnetopause Crossing (MPC) events
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            
        Returns:
            Dictionary containing MPC events
        """
        params = self._get_date_params(start_date, end_date)
        endpoint = f"{self.base_endpoint}/MPC"
        return self._make_request(endpoint, params)
    
    def get_radiation_belt_enhancements(self, start_date: Optional[str] = None, 
                                       end_date: Optional[str] = None) -> Dict[str, Any]:
        """
        Get Radiation Belt Enhancement (RBE) events
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            
        Returns:
            Dictionary containing RBE events
        """
        params = self._get_date_params(start_date, end_date)
        endpoint = f"{self.base_endpoint}/RBE"
        return self._make_request(endpoint, params)
    
    def get_high_speed_streams(self, start_date: Optional[str] = None, 
                              end_date: Optional[str] = None) -> Dict[str, Any]:
        """
        Get High Speed Stream (HSS) events
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            
        Returns:
            Dictionary containing HSS events
        """
        params = self._get_date_params(start_date, end_date)
        endpoint = f"{self.base_endpoint}/HSS"
        return self._make_request(endpoint, params)
    
    def _get_date_params(self, start_date: Optional[str], end_date: Optional[str]) -> Dict[str, str]:
        """Helper method to prepare date parameters"""
        params = {}
        
        if start_date:
            try:
                params['startDate'] = self._format_date(start_date)
            except ValueError:
                # Use default if invalid
                params['startDate'] = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
        else:
            params['startDate'] = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
        
        if end_date:
            try:
                params['endDate'] = self._format_date(end_date)
            except ValueError:
                # Use default if invalid
                params['endDate'] = datetime.now().strftime('%Y-%m-%d')
        else:
            params['endDate'] = datetime.now().strftime('%Y-%m-%d')
        
        return params
