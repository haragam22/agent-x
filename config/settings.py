import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    """Configuration settings for the Agent-X tool."""
    
    # General settings
    PROJECT_NAME = "Agent-X"
    VERSION = "1.0.0"
    DEBUG = os.getenv("DEBUG", "True").lower() == "true"

    # OpenAI API Key for LLM interactions
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    # Web Scraping & SEO settings
    USER_AGENT = os.getenv("USER_AGENT", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

    # Database (Optional: if you need to store data)
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///data.db")

    # LLM Model Configuration
    LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4")  # Change to "gpt-3.5-turbo" if needed
    LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "0.7"))
    LLM_MAX_TOKENS = int(os.getenv("LLM_MAX_TOKENS", "1000"))

    # Webpage Monitoring Configuration
    CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", "3600"))  # Default: 1 hour
    SEO_OPTIMIZATION_ENABLED = os.getenv("SEO_OPTIMIZATION_ENABLED", "True").lower() == "true"
    LINK_FIXING_ENABLED = os.getenv("LINK_FIXING_ENABLED", "True").lower() == "true"
    
    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Create an instance of Settings
settings = Settings()
