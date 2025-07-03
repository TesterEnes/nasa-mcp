"""
InSight Mars Weather API
"""
from .base import NASAAPIBase
from typing import Dict, Any


class MarsWeatherAPI(NASAAPIBase):
    """NASA InSight Mars Weather API client"""
    
    def __init__(self, api_key: str = "DEMO_KEY"):
        super().__init__(api_key)
        self.endpoint = f"{self.base_url}/insight_weather/"
    
    def get_weather(self) -> Dict[str, Any]:
        """
        Get Mars weather data from NASA InSight Weather API.
        Returns the latest available weather data from Mars.
        """
        params = {
            "feedtype": "json",
            "ver": "1.0"
        }
        
        try:
            data = self._make_request(self.endpoint, params)
            
            if "error" in data:
                return data
            
            # Get the latest sol (Martian day) data
            sol_keys = data.get("sol_keys", [])
            if not sol_keys:
                return {"error": "No weather data available"}
            
            # Get the most recent sol data
            latest_sol = sol_keys[-1]
            latest_data = data[latest_sol]
            
            # Extract weather information
            weather_info = {
                "sol": latest_sol,
                "first_utc": latest_data.get("First_UTC"),
                "last_utc": latest_data.get("Last_UTC"),
                "season": latest_data.get("Season"),
                "northern_season": latest_data.get("Northern_season"),
                "southern_season": latest_data.get("Southern_season")
            }
            
            # Extract temperature data (AT = Atmospheric Temperature)
            if "AT" in latest_data:
                temp_data = latest_data["AT"]
                weather_info["temperature"] = {
                    "average": temp_data.get("av"),
                    "minimum": temp_data.get("mn"),
                    "maximum": temp_data.get("mx"),
                    "unit": "Celsius"
                }
            
            # Extract pressure data (PRE = Pressure)
            if "PRE" in latest_data:
                pressure_data = latest_data["PRE"]
                weather_info["pressure"] = {
                    "average": pressure_data.get("av"),
                    "minimum": pressure_data.get("mn"),
                    "maximum": pressure_data.get("mx"),
                    "unit": "Pa"
                }
            
            # Extract wind data (HWS = Horizontal Wind Speed)
            if "HWS" in latest_data:
                wind_data = latest_data["HWS"]
                weather_info["wind_speed"] = {
                    "average": wind_data.get("av"),
                    "minimum": wind_data.get("mn"),
                    "maximum": wind_data.get("mx"),
                    "unit": "m/s"
                }
            
            # Extract wind direction data (WD = Wind Direction)
            if "WD" in latest_data and "most_common" in latest_data["WD"]:
                wind_dir = latest_data["WD"]["most_common"]
                weather_info["wind_direction"] = {
                    "compass_point": wind_dir.get("compass_point"),
                    "compass_degrees": wind_dir.get("compass_degrees")
                }
            
            return weather_info
            
        except Exception as e:
            return {"error": f"An error occurred: {str(e)}"}
