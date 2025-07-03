def get_mars_weather(api_key="DEMO_KEY"):
    """
    Get Mars weather data from NASA InSight Weather API.
    Returns the latest available weather data from Mars.
    """
    import requests

    # Define the NASA InSight Weather API endpoint
    api_url = "https://api.nasa.gov/insight_weather/"
    params = {
        "api_key": api_key,
        "feedtype": "json",
        "ver": "1.0"
    }

    try:
        # Make the API request
        response = requests.get(api_url, params=params)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

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

        else:
            return {"error": f"API request failed with status code: {response.status_code}"}

    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}


# Test function
if __name__ == "__main__":
    print("Testing NASA Mars Weather API...")
    result = get_mars_weather()
    print("Result:")
    import json
    print(json.dumps(result, indent=2))
