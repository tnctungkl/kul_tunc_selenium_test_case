from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from config.env import ENV
from config.settings import IMPLICIT_WAIT

# Factory method to create WebDriver instances based on environment configuration.
def create_driver():
    # Create a WebDriver instance based on the specified browser in the environment configuration.
    if ENV.browser.lower() == "chrome":
        options = ChromeOptions()
        # Configure Chrome options based on environment settings.
        if ENV.headless:
            options.add_argument("--headless=new")  # Run 'Chrome' in headless mode.
            options.add_argument("--window-size=1920,1080")  # FullHD resolution.
            options.add_argument("--no-sandbox")  # Bypass OS security model.
            options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems.

        # Initialize Chrome WebDriver with the specified options.
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(
            service=service,
            options=options,
        )

    else:
        # If the specified browser is not supported, raise an error.
        raise NotImplementedError(f"Browser '{ENV.browser}' is not supported yet.")
    
    # Set implicit wait time for the WebDriver instance.
    driver.implicitly_wait(IMPLICIT_WAIT)
    return driver
