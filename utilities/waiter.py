from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.settings import EXPLICIT_WAIT

# Utility methods for explicit waits in Selenium WebDriver.
def wait_for_visibility(driver, locator, timeout: int | None = None):
    t = timeout or EXPLICIT_WAIT
    return WebDriverWait(driver, t).until(EC.visibility_of_element_located(locator))

# Utility method to wait for an element to become invisible.
def wait_for_invisibility(driver, locator, timeout: int | None = None):
    t = timeout or EXPLICIT_WAIT
    return WebDriverWait(driver, t).until(EC.invisibility_of_element_located(locator))
