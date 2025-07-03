"""
NASA APIs Integration Module
Provides access to all NASA API endpoints through a unified interface
"""

from nasa_apis.apod import APODAPI
from nasa_apis.asteroids import AsteroidsAPI
from nasa_apis.mars_weather import MarsWeatherAPI
from nasa_apis.mars_rover import MarsRoverAPI
from nasa_apis.earth import EarthAPI
from nasa_apis.epic import EPICAPI
from nasa_apis.eonet import EONETAPI
from nasa_apis.donki import DONKIAPI
from nasa_apis.nasa_library import NASALibraryAPI
from nasa_apis.exoplanet import ExoplanetAPI


class NASAAPIManager:
    """Unified manager for all NASA APIs"""

    def __init__(self, api_key: str = "DEMO_KEY"):
        self.api_key = api_key

        # Initialize all API clients
        self.apod = APODAPI(api_key)
        self.asteroids = AsteroidsAPI(api_key)
        self.mars_weather = MarsWeatherAPI(api_key)
        self.mars_rover = MarsRoverAPI(api_key)
        self.earth = EarthAPI(api_key)
        self.epic = EPICAPI(api_key)
        self.eonet = EONETAPI(api_key)
        self.donki = DONKIAPI(api_key)
        self.nasa_library = NASALibraryAPI(api_key)
        self.exoplanet = ExoplanetAPI(api_key)


# Legacy function for backward compatibility
def get_mars_weather(api_key="DEMO_KEY"):
    """Legacy function - use MarsWeatherAPI class instead"""
    api = MarsWeatherAPI(api_key)
    return api.get_weather()


# Test function
if __name__ == "__main__":
    print("Testing NASA API Manager...")
    manager = NASAAPIManager()

    # Test Mars Weather
    print("\n=== Mars Weather ===")
    result = manager.mars_weather.get_weather()
    print("Result:")
    import json
    print(json.dumps(result, indent=2)[:500] + "...")

    # Test APOD
    print("\n=== APOD ===")
    apod_result = manager.apod.get_picture_of_the_day()
    if "error" not in apod_result:
        print(f"Title: {apod_result.get('title', 'N/A')}")
        print(f"Date: {apod_result.get('date', 'N/A')}")
        print(f"Explanation: {apod_result.get('explanation', 'N/A')[:100]}...")
    else:
        print(f"Error: {apod_result['error']}")

    print("\nAll APIs initialized successfully!")
