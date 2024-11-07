from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


class DriverSetup:
    """Handles the setup and teardown of the WebDriver."""
    def __init__(self):
        options = Options()
        # Maximize the window to ensure that all elements are visible and prevent blocking
        options.add_argument("--start-maximized")
        # Ignore SSL certificate errors since we're not concerned with security
        options.add_argument("--ignore-certificate-errors")
        # Disable loading of images to speed up the scraping process
        options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})

        # Initialize the WebDriver
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)

    def close(self):
        """Close the WebDriver."""
        self.driver.quit()