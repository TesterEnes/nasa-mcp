"""
Exoplanet Archive API
"""
from .base import NASAAPIBase
from typing import Dict, Any, Optional
import urllib.parse


class ExoplanetAPI(NASAAPIBase):
    """NASA Exoplanet Archive API client"""
    
    def __init__(self, api_key: str = "DEMO_KEY"):
        super().__init__(api_key)
        # Exoplanet Archive uses different base URL and doesn't require API key
        self.base_endpoint = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"
    
    def query_planets(self, select: str = "*", where: Optional[str] = None, 
                     order_by: Optional[str] = None, limit: Optional[int] = None) -> Dict[str, Any]:
        """
        Query exoplanet data using ADQL
        
        Args:
            select: Columns to select (default: all)
            where: WHERE clause conditions
            order_by: ORDER BY clause
            limit: LIMIT number of results
            
        Returns:
            Dictionary containing exoplanet data
        """
        query = f"SELECT {select} FROM ps"  # ps = Planetary Systems table
        
        if where:
            query += f" WHERE {where}"
        if order_by:
            query += f" ORDER BY {order_by}"
        if limit:
            query += f" LIMIT {limit}"
        
        params = {
            'query': query,
            'format': 'json'
        }
        
        return self._make_external_request(self.base_endpoint, params)
    
    def get_confirmed_planets(self, limit: int = 100) -> Dict[str, Any]:
        """
        Get confirmed exoplanets
        
        Args:
            limit: Maximum number of results
            
        Returns:
            Dictionary containing confirmed exoplanet data
        """
        return self.query_planets(
            select="pl_name,hostname,discoverymethod,disc_year,pl_orbper,pl_bmasse,pl_rade,st_dist",
            where="default_flag=1",
            order_by="disc_year DESC",
            limit=limit
        )
    
    def search_planets_by_name(self, planet_name: str) -> Dict[str, Any]:
        """
        Search for planets by name
        
        Args:
            planet_name: Planet name to search for
            
        Returns:
            Dictionary containing matching planets
        """
        where_clause = f"pl_name LIKE '%{planet_name}%'"
        return self.query_planets(where=where_clause)
    
    def get_planets_by_discovery_method(self, method: str, limit: int = 50) -> Dict[str, Any]:
        """
        Get planets by discovery method
        
        Args:
            method: Discovery method (e.g., 'Transit', 'Radial Velocity')
            limit: Maximum number of results
            
        Returns:
            Dictionary containing planets discovered by specified method
        """
        where_clause = f"discoverymethod='{method}'"
        return self.query_planets(
            where=where_clause,
            order_by="disc_year DESC",
            limit=limit
        )
    
    def get_habitable_zone_planets(self, limit: int = 50) -> Dict[str, Any]:
        """
        Get potentially habitable planets
        
        Args:
            limit: Maximum number of results
            
        Returns:
            Dictionary containing potentially habitable planets
        """
        # Simple habitable zone criteria: Earth-like size and temperature
        where_clause = "pl_rade BETWEEN 0.5 AND 2.0 AND pl_eqt BETWEEN 200 AND 350"
        return self.query_planets(
            select="pl_name,hostname,pl_rade,pl_bmasse,pl_orbper,pl_eqt,st_dist,disc_year",
            where=where_clause,
            order_by="pl_eqt ASC",
            limit=limit
        )
    
    def get_recent_discoveries(self, years_back: int = 5, limit: int = 100) -> Dict[str, Any]:
        """
        Get recently discovered exoplanets
        
        Args:
            years_back: Number of years back from current year
            limit: Maximum number of results
            
        Returns:
            Dictionary containing recent discoveries
        """
        from datetime import datetime
        current_year = datetime.now().year
        start_year = current_year - years_back
        
        where_clause = f"disc_year >= {start_year}"
        return self.query_planets(
            where=where_clause,
            order_by="disc_year DESC",
            limit=limit
        )
