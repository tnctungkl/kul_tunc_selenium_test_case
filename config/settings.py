import os
from pathlib import Path

# Root directory of the project.
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Base URL of the application.
BASE_URL = os.getenv("BASE_URL", "https://piratesquad.rocks")

# Default timeouts (in seconds) for waits.
IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "5"))
EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "10"))

# Browser configuration (chrome(based), firefox, etc. + headless mode).
BROWSER = os.getenv("BROWSER", "chrome")
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"

# Paths: Screenshots, logs, and data.
SCREENSHOT_DIR = PROJECT_ROOT / "screenshots"
LOG_DIR = PROJECT_ROOT / "logs"
DATA_DIR = PROJECT_ROOT / "data"

# Ensure all directories exist.
SCREENSHOT_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

# Campaig can be overridden from .env or .JSON .
DEFAULT_CAMPAIGN_ID = os.getenv("CAMPAIGN_ID", "16087")
DEFAULT_CUSTOM_RULE_ID = os.getenv("CUSTOM_RULE_ID", "3677")
DEFAULT_LANGUAGE = os.getenv("CAMPAIGN_LANG", "tr_TR")

# Viewport sizes used for responsive checks.
VIEWPORT_DESKTOP = (1920, 1080)
VIEWPORT_TABLET = (1024, 768)
VIEWPORT_MOBILE = (414, 896)