from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

class DriverSetup:
    """Handles the setup and teardown of the WebDriver."""
    def __init__(self):
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--ignore-certificate-errors")
        options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)

    def close(self):
        """Close the WebDriver."""
        self.driver.quit()