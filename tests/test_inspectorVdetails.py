import allure
from config.settings import BASE_URL
from pages.inspector import InspectorPanel
from pages.page_products import ProductPage

# Test class for verifying inspector details match campaign data.
class TestInspectorDetails:
    # Test to verify inspector details match expected campaign data.
    @allure.description("Verify inspector details (Campaign ID, Language, Custom Rule) match expected campaign data.")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_inspector_details_match_campaign_data(self, driver, test_data):
        with allure.step("Construct product URL from BASE_URL + test_data JSON"):
            product_url = BASE_URL + test_data["product_page"]["url"] # example; "/products/sample-product"

        product = ProductPage(driver)
        inspector = InspectorPanel(driver)

        # Open product page and wait for popup to become visible.
        with allure.step("Open product page and wait for popup to become visible"):
            product.open(product_url)
            product.wait_for_popup_visible()

        # Ensure inspector is visible and open 'Details' section of inspector.
        with allure.step("Ensure inspector is visible and open 'Details' section"):
            inspector.wait_until_visible()
            inspector.open_details()

        # Read expected campaign values from test_data JSON for assertions.
        with allure.step("Read expected campaign values from test_data JSON"):
            expected_id = str(test_data["campaign"]["id"]) # Verify Campaign ID.
            expected_lang = test_data["campaign"]["language"] # Verify Campaign Language.
            expected_rule = str(test_data["campaign"]["custom_rule_id"]) # Verify Custom Rule ID.

        # Assertions for inspector details matching expected campaign metadata.
        with allure.step("Assert inspector details match expected campaign metadata"):
            # Assertions for inspector details.
            assert inspector.get_details_campaign_id() == expected_id
            assert inspector.get_details_language() == expected_lang
            assert expected_rule in inspector.get_details_custom_rule()
