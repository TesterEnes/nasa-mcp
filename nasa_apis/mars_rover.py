"""
Mars Rover Photos API
"""
from .base import NASAAPIBase
from typing import Dict, Any, Optional, List


class MarsRoverAPI(NASAAPIBase):
    """NASA Mars Rover Photos API client"""
    
    def __init__(self, api_key: str = "DEMO_KEY"):
        super().__init__(api_key)
        self.base_endpoint = f"{self.base_url}/mars-photos/api/v1/rovers"
        self.rovers = ["curiosity", "opportunity", "spirit", "perseverance"]
        self.cameras = {
            "curiosity": ["FHAZ", "RHAZ", "MAST", "CHEMCAM", "MAHLI", "MARDI", "NAVCAM"],
            "opportunity": ["FHAZ", "RHAZ", "NAVCAM", "PANCAM", "MINITES"],
            "spirit": ["FHAZ", "RHAZ", "NAVCAM", "PANCAM", "MINITES"],
            "perseverance": ["EDL_RUCAM", "EDL_RDCAM", "EDL_DDCAM", "EDL_PUCAM1", "EDL_PUCAM2", 
                           "NAVCAM_LEFT", "NAVCAM_RIGHT", "MCZ_LEFT", "MCZ_RIGHT", "FRONT_HAZCAM_LEFT_A",
                           "FRONT_HAZCAM_RIGHT_A", "REAR_HAZCAM_LEFT", "REAR_HAZCAM_RIGHT", "SKYCAM", "SHERLOC_WATSON"]
        }
    
    def get_photos_by_sol(self, rover: str, sol: int, camera: Optional[str] = None, page: int = 1) -> Dict[str, Any]:
        """
        Get rover photos by Martian sol (day)
        
        Args:
            rover: Rover name (curiosity, opportunity, spirit, perseverance)
            sol: Martian sol number
            camera: Camera name (optional)
            page: Page number for pagination
            
        Returns:
            Dictionary containing rover photos
        """
        if rover.lower() not in self.rovers:
            return {"error": f"Invalid rover. Must be one of: {', '.join(self.rovers)}"}
        
        params = {
            "sol": sol,
            "page": page
        }
        
        if camera:
            if rover.lower() in self.cameras and camera.upper() not in self.cameras[rover.lower()]:
                return {"error": f"Invalid camera for {rover}. Available cameras: {', '.join(self.cameras[rover.lower()])}"}
            params["camera"] = camera.upper()
        
        endpoint = f"{self.base_endpoint}/{rover.lower()}/photos"
        return self._make_request(endpoint, params)
    
    def get_photos_by_earth_date(self, rover: str, earth_date: str, camera: Optional[str] = None, page: int = 1) -> Dict[str, Any]:
        """
        Get rover photos by Earth date
        
        Args:
            rover: Rover name
            earth_date: Earth date in YYYY-MM-DD format
            camera: Camera name (optional)
            page: Page number for pagination
            
        Returns:
            Dictionary containing rover photos
        """
        if rover.lower() not in self.rovers:
            return {"error": f"Invalid rover. Must be one of: {', '.join(self.rovers)}"}
        
        try:
            earth_date = self._format_date(earth_date)
        except ValueError as e:
            return {"error": str(e)}
        
        params = {
            "earth_date": earth_date,
            "page": page
        }
        
        if camera:
            if rover.lower() in self.cameras and camera.upper() not in self.cameras[rover.lower()]:
                return {"error": f"Invalid camera for {rover}. Available cameras: {', '.join(self.cameras[rover.lower()])}"}
            params["camera"] = camera.upper()
        
        endpoint = f"{self.base_endpoint}/{rover.lower()}/photos"
        return self._make_request(endpoint, params)
    
    def get_latest_photos(self, rover: str) -> Dict[str, Any]:
        """
        Get latest photos from rover
        
        Args:
            rover: Rover name
            
        Returns:
            Dictionary containing latest rover photos
        """
        if rover.lower() not in self.rovers:
            return {"error": f"Invalid rover. Must be one of: {', '.join(self.rovers)}"}
        
        endpoint = f"{self.base_endpoint}/{rover.lower()}/latest_photos"
        return self._make_request(endpoint)
    
    def get_manifest(self, rover: str) -> Dict[str, Any]:
        """
        Get rover mission manifest
        
        Args:
            rover: Rover name
            
        Returns:
            Dictionary containing rover mission manifest
        """
        if rover.lower() not in self.rovers:
            return {"error": f"Invalid rover. Must be one of: {', '.join(self.rovers)}"}
        
        endpoint = f"{self.base_endpoint}/{rover.lower()}"
        return self._make_request(endpoint)
