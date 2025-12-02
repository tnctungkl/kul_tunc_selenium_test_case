import allure
from pages.page_products import ProductPage

from config.settings import (
    BASE_URL,
    VIEWPORT_DESKTOP,
    VIEWPORT_TABLET,
    VIEWPORT_MOBILE,
)

# Test class for verifying popup responsiveness on different viewports.
class TestPopupResponsiveness:
    # Helper method to assert popup is fully within viewport.
    def _assert_popup_fully_in_viewport(self, driver, popup_element):
        size = driver.get_window_size() # Get current viewport size.
        viewport_height = size["height"] # Get viewport height.

        rect = popup_element.rect # Get popup element rectangle.
        top = rect["y"] # Get popup top position.
        bottom = rect["y"] + rect["height"] # Get popup bottom height.
        
        assert top >= 0, "Popup top is above the viewport." # Verify popup top is within viewport.
        assert bottom <= viewport_height, "Popup bottom is below the viewport." # Verify popup bottom is within viewport.

    # Test to verify popup responsiveness on common viewports.
    @allure.description("Validate popup responsiveness on desktop, tablet, and mobile viewports.")
    @allure.severity(allure.severity_level.NORMAL)
    def test_popup_responsive_on_common_viewports(self, driver, test_data):
        # Construct product page URL from BASE_URL and JSON test data file.
        with allure.step("Construct product page URL from BASE_URL + JSON file"):
            url = BASE_URL + test_data["product_page"]["url"] # example; "/products/sample-product".

        product = ProductPage(driver)

        # Test on desktop, tablet, and mobile viewports.
        for width, height in (
            VIEWPORT_DESKTOP,
            VIEWPORT_TABLET,
            VIEWPORT_MOBILE,
        ):
            # Test responsiveness in the current viewport size.
            with allure.step(f"Testing responsiveness in viewport: {width}x{height}"):
                driver.set_window_size(width, height)
                product.open(url)
                # Wait for popup to be visible and assert it's fully within viewport bounds.
                popup = product.wait_for_popup_visible()
                self._assert_popup_fully_in_viewport(driver, popup)
