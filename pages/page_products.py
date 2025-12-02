from selenium.webdriver.common.by import By

from pages.page_base import BasePage
from utilities.waiter import wait_for_visibility

# Product Page Object Model.
class ProductPage(BasePage):
    # Selectors for popup and cart elements.
    POPUP_CONTAINER = (By.CSS_SELECTOR, "div.onsite-experiment-popup") # Popup container selector.
    POPUP_CLOSE_BUTTON = (By.CSS_SELECTOR, "div.onsite-experiment-popup button.close") # Popup close button selector.
    POPUP_ADD_TO_CART_BUTTON = (
        By.CSS_SELECTOR,
        "div.onsite-experiment-popup button.add-to-cart", # Popup add to cart button selector.
    )
    POPUP_PRODUCT_NAME = (
        By.CSS_SELECTOR,
        "div.onsite-experiment-popup .product-title", # Popup product name selector.
    )
    
    CART_COUNT_BADGE = (By.CSS_SELECTOR, "span.cart-products-count") # Cart count badge selector.

    # Methods to interact with popup and cart elements.
    def wait_for_popup_visible(self):
        popup = wait_for_visibility(self.driver, self.POPUP_CONTAINER)
        self.take_screenshot("popup_visible_on_product_page") # Screenshots for verification.
        return popup
    
    # Method to close the popup with close button.
    def close_popup(self):
        self.driver.find_element(*self.POPUP_CLOSE_BUTTON).click()

    # Method to add product to cart from popup with add to cart button.
    def click_add_to_cart_on_popup(self):
        self.driver.find_element(*self.POPUP_ADD_TO_CART_BUTTON).click()

    # Method to get product name from popup with proper whitespace handling.
    def get_popup_product_name(self) -> str:
        return self.driver.find_element(*self.POPUP_PRODUCT_NAME).text.strip()

    # Method to get the current cart count as an integer with default handling.
    def get_cart_count(self) -> int:
        badge_text = self.driver.find_element(*self.CART_COUNT_BADGE).text.strip() # Get cart count text.
        return int(badge_text or "0") # Convert to integer, default to 0 if empty.
