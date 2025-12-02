from selenium.webdriver.common.by import By

from pages.page_base import BasePage
from utilities.waiter import wait_for_visibility

# Inspector Page Object.
class InspectorPanel(BasePage):
    # Locators.
    STATUS_BADGE = (By.CSS_SELECTOR, "span.inspector-status-badge")  # Visible / Not Visible status.
    CAMPAIGN_SELECT = (By.CSS_SELECTOR, "select.inspector-campaign-select") # Campaign dropdown.
    SHOW_INSTANTLY_BUTTON = (By.CSS_SELECTOR, "button.show-instantly") # Show Instantly button.
    DETAILS_LINK = (By.LINK_TEXT, "DETAILS") # Link to open details popup.

    # Details popup
    DETAILS_CAMPAIGN_ID = (By.CSS_SELECTOR, "div.campaign-info span.campaign-id") # Campaign ID 'in' details popup.
    DETAILS_LANGUAGE = (By.CSS_SELECTOR, "div.campaign-info span.campaign-lang") # Language 'in' details popup.
    DETAILS_CUSTOM_RULE = (By.CSS_SELECTOR, "div.campaign-info span.custom-rule") # Custom rule 'in' details popup.

    # Variable visible Methods.
    def wait_until_visible(self):
        panel = wait_for_visibility(self.driver, self.STATUS_BADGE) # Wait until the status badge is visible.
        self.take_screenshot("inspector_visible") # Take screenshots for verification.
        return panel

    # Action Methods.
    def get_status_text(self) -> str:
        return self.driver.find_element(*self.STATUS_BADGE).text.strip() # Get the status text.

    # Select campaign by visible text details.
    def open_details(self):
        self.driver.find_element(*self.DETAILS_LINK).click() # Click on DETAILS link.

    # Details popup Methods.
    def get_details_campaign_id(self) -> str:
        return self.driver.find_element(*self.DETAILS_CAMPAIGN_ID).text.strip() # Get campaign ID 'from' details popup.

    # Get language from details popup.
    def get_details_language(self) -> str:
        return self.driver.find_element(*self.DETAILS_LANGUAGE).text.strip() # Get language 'from' details popup.

    # Get custom rule from details popup.
    def get_details_custom_rule(self) -> str:
        return self.driver.find_element(*self.DETAILS_CUSTOM_RULE).text.strip() # Get custom rule 'from' details popup.
