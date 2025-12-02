from datetime import datetime
from pathlib import Path
from selenium.webdriver.remote.webdriver import WebDriver

from config.settings import SCREENSHOT_DIR
from utilities.logger import get_logger

# Base page class for all page objects.
class BasePage:
    # Initialize with WebDriver and logger.
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)

    # Navigate to a specified URL.
    def open(self, url: str):
        self.logger.info("Navigating to URL: %s", url)
        self.driver.get(url)

    # Capture a screenshot with a semantic name.
    def take_screenshot(self, name: str):
        # Generate a unique filename with timestamp.
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S_%f") # UTC timestamp for uniqueness.
        filename = f"{name}_{timestamp}.png" # Semantic filename.
        path = Path(SCREENSHOT_DIR, filename) # Full path for the screenshots.
        self.driver.save_screenshot(str(path)) # Save the screenshot.
        self.logger.info("Screenshot captured: %s", path) # Log the screenshot capture.
        return path
