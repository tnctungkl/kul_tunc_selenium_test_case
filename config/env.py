import os
from dataclasses import dataclass

# Environment configuration dataclass part.
@dataclass(frozen=True)
class EnvironmentConfig:
    base_url: str
    browser: str
    headless: bool
    environment_name: str

# Function to load environment configuration from environment variables.
def load_environment_config() -> EnvironmentConfig:
    env_name = os.getenv("TEST_ENV", "local")
    # WARNING: You can add more environment-specific logic here if needed.
    return EnvironmentConfig(
        # WARNING: Default values can be overridden by environment variables.
        base_url=os.getenv("BASE_URL", "https://piratesquad.rocks"), # Default base URL.
        browser=os.getenv("BROWSER", "chrome"), # Default browser.
        headless=os.getenv("HEADLESS", "true").lower() == "true", # Default headless mode.
        environment_name=env_name,
    )

# Load the environment configuration at module import time.
ENV = load_environment_config()