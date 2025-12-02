from selenium.webdriver.common.by import By

from pages.page_base import BasePage

# Home Page Object Model.
class HomePage(BasePage):
    # Locators.
    POPUP_CONTAINER = (By.CSS_SELECTOR, "div.onsite-experiment-popup") # Example popup container.
    # Locator for a specific product tile.
    PRODUCT_TILE = (
        By.CSS_SELECTOR,
        "section#popular-products a.product-thumbnail[href*='the-adventure-begins']", # Example product tile link.
    )
    # Home URL Methods.
    def open_home(self, base_url: str):
        self.open(base_url)
    # Navigate to a specific product from the home page.
    def go_to_product_from_home(self):
        product = self.driver.find_element(*self.PRODUCT_TILE)
        product.click()
