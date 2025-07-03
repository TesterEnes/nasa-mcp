from mcp.server.fastmcp import FastMCP
from app import get_mars_weather

# Initialize MCP server
mcp = FastMCP("nasa-mars-weather-mcp")

@mcp.tool()
async def get_mars_weather_data(api_key: str = "DEMO_KEY") -> dict:
    """
    Get the latest Mars weather data from NASA InSight Weather API.

    Args:
        api_key: NASA API key (defaults to DEMO_KEY for testing)

    Returns:
        Dictionary containing Mars weather information including:
        - sol: Martian day number
        - temperature: min/max/average temperatures in Celsius
        - pressure: atmospheric pressure data in Pascals
        - wind_speed: wind speed data in m/s
        - wind_direction: wind direction information
        - season: Martian season information
        - UTC timestamps for data collection period
    """
    # Call the function from app.py
    result = get_mars_weather(api_key)
    return result

if __name__ == "__main__":
    mcp.run(transport="stdio")