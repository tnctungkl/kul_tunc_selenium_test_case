import allure
import urllib.parse

from config.settings import BASE_URL
from pages.page_home import HomePage
from pages.page_products import ProductPage
from pages.inspector import InspectorPanel
from utilities.waiter import wait_for_invisibility

# Test class for verifying popup visibility on different pages.
class TestPopupVisibility:
    # Test to verify popup is not visible on home page.
    @allure.description("Verify that the campaign popup is NOT visible on the home page.")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_popup_not_visible_on_home_page(self, driver):
        home = HomePage(driver)
        # Open home page URL and wait for loading indicators to disappear.
        with allure.step("Assert that campaign popup is NOT visible on home page"):
            home.logger.info("Asserting that campaign popup is not visible on home page.")
            popup_elements = driver.find_elements(*home.POPUP_CONTAINER)
            # Verify that no popup elements are displayed.
            assert not any(e.is_displayed() for e in popup_elements), (
                "Campaign popup should not be visible on the home page." # Verify popup is not visible.
            )
    # Test to verify popup visibility on product page and inspector status.
    @allure.description("Verify popup visibility on product page and inspector status changes to 'Visible'.") # Test to verify popup visibility on product page.
    @allure.severity(allure.severity_level.BLOCKER)
    def test_popup_visible_on_product_page_and_inspector_status(self, driver, test_data):
        
        # Build product page URL.
        with allure.step("Build product page URL using urljoin"):
            product_page_url = urllib.parse.urljoin(
                BASE_URL, test_data["product_page"]["url"] # example; "/products/sample-product"
            )
        
        product = ProductPage(driver)
        inspector = InspectorPanel(driver)

        # Open product page and wait for popup to be visible.
        with allure.step("Open product page"):
            product.open(product_page_url)

        # Wait for any loading indicators to disappear.
        with allure.step("Wait for popup to become visible on product page"):
            popup = product.wait_for_popup_visible()
            assert popup.is_displayed(), "Popup container is not visible on product page." # Verify popup is visible.
        # Wait for loading indicators to disappear.
        with allure.step("Ensure inspector panel is visible and status is 'Visible'"):
            inspector.wait_until_visible()
            status_text = inspector.get_status_text().lower()
            # Verify inspector status is 'Visible'.
            assert "visible" in status_text, (
                f"Inspector status is not 'Visible'. Actual: {status_text}" # Verify inspector status.
            )
