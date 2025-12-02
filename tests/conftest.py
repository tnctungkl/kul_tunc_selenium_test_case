import json
import pytest
from datetime import datetime
from pathlib import Path

from config.env import ENV
from config.settings import DATA_DIR, SCREENSHOT_DIR
from utilities.driver_factory import create_driver

# Part of Fixtures.
@pytest.fixture(scope="session")
# Load test data from a JSON file.
def test_data():
    with open(Path(DATA_DIR, "test_data.json"), encoding="utf-8") as f:
        return json.load(f)

# Fixture to create and yield a web driver instance.
@pytest.fixture
def driver():
    driver = create_driver() # Initialize the web driver.
    driver.get(ENV.base_url) # Navigate to the base URL.
    yield driver # Provide the driver to the test.
    driver.quit()

# Pytest hook to capture screenshots on test failure.
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
# Capture screenshots on test failure.
def pytest_runtest_makereport(item, call):
    outcome = yield # Execute all other hooks to obtain the report object.
    report = outcome.get_result() # Get the test report.
    # If the test failed during the call phase, capture a screenshot.
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver") # Access the driver fixture.
        if driver:
            SCREENSHOT_DIR.mkdir(exist_ok=True) # Ensure the screenshot directory exists.
            timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S_%f") # Generate a timestamp.
            filename = f"FAILED_{item.name}_{timestamp}.png" # Create a unique custom filename.
            path = Path(SCREENSHOT_DIR, filename) # Define the full path for the screenshot.
            driver.save_screenshot(str(path)) # Save the screenshot.
            print(f"\n[pytest] Failure screenshot saved to: {path}") # Log the screenshot path.
