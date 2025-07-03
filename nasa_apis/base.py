"""
Base class for NASA API clients
"""
import requests
from typing import Dict, Any, Optional
import time
import logging
from datetime import datetime
from config import get_config


class NASAAPIBase:
    """Base class for all NASA API clients"""

    def __init__(self, api_key: str = "DEMO_KEY"):
        self.config = get_config()
        self.api_key = api_key or self.config.get_nasa_api_key()
        self.session = requests.Session()
        self.base_url = "https://api.nasa.gov"

        # Setup logging
        logging.basicConfig(
            level=getattr(logging, self.config.log_level),
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(self.__class__.__name__)
        
    def _make_request(self, url: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Make HTTP request with error handling and rate limiting
        """
        if params is None:
            params = {}

        # Add API key to params
        params['api_key'] = self.api_key

        # Log request
        self.logger.debug(f"Making request to {url} with params: {params}")

        max_retries = self.config.max_retries
        retry_delay = self.config.retry_delay
        timeout = self.config.request_timeout

        for attempt in range(max_retries + 1):
            try:
                response = self.session.get(url, params=params, timeout=timeout)

                # Handle rate limiting
                if response.status_code == 429:
                    retry_after = int(response.headers.get('Retry-After', 60))
                    self.logger.warning(f"Rate limited. Waiting {retry_after} seconds...")
                    time.sleep(retry_after)
                    continue

                # Handle other HTTP errors
                if response.status_code >= 400:
                    error_msg = f"HTTP {response.status_code}: {response.text[:200]}"
                    self.logger.error(error_msg)

                    if attempt < max_retries and response.status_code >= 500:
                        # Retry on server errors
                        self.logger.info(f"Retrying in {retry_delay} seconds... (attempt {attempt + 1}/{max_retries})")
                        time.sleep(retry_delay)
                        continue

                    return {"error": error_msg}

                # Success
                self.logger.debug(f"Request successful: {response.status_code}")
                return response.json()

            except requests.exceptions.Timeout:
                error_msg = f"Request timeout after {timeout} seconds"
                self.logger.error(error_msg)

                if attempt < max_retries:
                    self.logger.info(f"Retrying in {retry_delay} seconds... (attempt {attempt + 1}/{max_retries})")
                    time.sleep(retry_delay)
                    continue

                return {"error": error_msg}

            except requests.exceptions.RequestException as e:
                error_msg = f"Request failed: {str(e)}"
                self.logger.error(error_msg)

                if attempt < max_retries:
                    self.logger.info(f"Retrying in {retry_delay} seconds... (attempt {attempt + 1}/{max_retries})")
                    time.sleep(retry_delay)
                    continue

                return {"error": error_msg}

            except Exception as e:
                error_msg = f"Unexpected error: {str(e)}"
                self.logger.error(error_msg)
                return {"error": error_msg}

        return {"error": "Max retries exceeded"}
    
    def _make_external_request(self, url: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Make HTTP request to external APIs (non-NASA)
        """
        if params is None:
            params = {}
            
        try:
            response = self.session.get(url, params=params, timeout=30)
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            return {"error": f"Request failed: {str(e)}"}
        except Exception as e:
            return {"error": f"An error occurred: {str(e)}"}

    def _format_date(self, date_str: str) -> str:
        """Validate and format date string"""
        try:
            # Try to parse the date to validate format
            datetime.strptime(date_str, '%Y-%m-%d')
            return date_str
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format")
