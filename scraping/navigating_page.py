from selenium.webdriver.support import expected_conditions as EC

from scraping.wait_driver import WaitDriver


class PageNavigator:
    """Handles page navigation and interaction."""
    def __init__(self, driver_setup):
        self.driver = driver_setup
        self.wait = WaitDriver(driver_setup).wait

    def open_url(self, url):
        self.driver.get(url)

    def wait_for_element(self, selector_type, selector_value):
        return self.wait.until(EC.visibility_of_element_located((selector_type, selector_value)))

    def click_element(self, element):
        element.click()

    def go_back(self):
        self.driver.back()
