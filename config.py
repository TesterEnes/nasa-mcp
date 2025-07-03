"""
Configuration management for NASA APIs MCP Server
"""
import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Configuration class for NASA APIs"""
    
    def __init__(self):
        # NASA API Configuration
        self.nasa_api_key = os.getenv('NASA_API_KEY', 'DEMO_KEY')
        
        # Rate limiting configuration
        self.rate_limit_requests_per_minute = int(os.getenv('RATE_LIMIT_RPM', '60'))
        self.rate_limit_requests_per_hour = int(os.getenv('RATE_LIMIT_RPH', '1000'))
        
        # Request timeout configuration
        self.request_timeout = int(os.getenv('REQUEST_TIMEOUT', '30'))
        
        # Retry configuration
        self.max_retries = int(os.getenv('MAX_RETRIES', '3'))
        self.retry_delay = int(os.getenv('RETRY_DELAY', '1'))
        
        # Cache configuration
        self.enable_cache = os.getenv('ENABLE_CACHE', 'false').lower() == 'true'
        self.cache_ttl = int(os.getenv('CACHE_TTL', '300'))  # 5 minutes default
        
        # Logging configuration
        self.log_level = os.getenv('LOG_LEVEL', 'INFO')
        self.log_file = os.getenv('LOG_FILE', 'nasa_apis.log')
        
        # MCP Server configuration
        self.mcp_server_name = os.getenv('MCP_SERVER_NAME', 'nasa-apis-mcp')
        
    def get_nasa_api_key(self) -> str:
        """Get NASA API key"""
        return self.nasa_api_key
    
    def is_demo_key(self) -> bool:
        """Check if using demo key"""
        return self.nasa_api_key == 'DEMO_KEY'
    
    def get_rate_limits(self) -> dict:
        """Get rate limiting configuration"""
        return {
            'requests_per_minute': self.rate_limit_requests_per_minute,
            'requests_per_hour': self.rate_limit_requests_per_hour
        }
    
    def get_request_config(self) -> dict:
        """Get request configuration"""
        return {
            'timeout': self.request_timeout,
            'max_retries': self.max_retries,
            'retry_delay': self.retry_delay
        }
    
    def get_cache_config(self) -> dict:
        """Get cache configuration"""
        return {
            'enabled': self.enable_cache,
            'ttl': self.cache_ttl
        }


# Global configuration instance
config = Config()


def get_config() -> Config:
    """Get global configuration instance"""
    return config


def validate_config() -> dict:
    """Validate configuration and return status"""
    issues = []
    warnings = []
    
    # Check API key
    if config.is_demo_key():
        warnings.append("Using DEMO_KEY - limited to 30 requests per hour")
    
    # Check rate limits
    if config.rate_limit_requests_per_minute > 60:
        warnings.append("Rate limit per minute is high - may cause API throttling")
    
    # Check timeout
    if config.request_timeout < 10:
        warnings.append("Request timeout is very low - may cause timeouts")
    elif config.request_timeout > 60:
        warnings.append("Request timeout is very high - may cause slow responses")
    
    # Check retry configuration
    if config.max_retries > 5:
        warnings.append("Max retries is high - may cause slow responses on failures")
    
    return {
        'valid': len(issues) == 0,
        'issues': issues,
        'warnings': warnings,
        'config': {
            'nasa_api_key': '***HIDDEN***' if not config.is_demo_key() else 'DEMO_KEY',
            'rate_limits': config.get_rate_limits(),
            'request_config': config.get_request_config(),
            'cache_config': config.get_cache_config()
        }
    }
