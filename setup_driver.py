from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

class DriverSetup:
    """Handles the setup and teardown of the WebDriver."""
    def __init__(self):

        """
        if you create a different class for browser initiation,
        create a separate options based on user preference as parameter.

        example:
        the basic settings that apply to all browser instance is start-maximized, 
        headless is optional, etc

        example:
        class DriverSetup:
            def __init__(self, is_headless):
                if headless:
                    options.add_argument.......
        """
        options = Options()
        options.add_argument("--start-maximized") # Sometimes, adding explanation on why we add this argument is helpful if others wanted to edit this code, 
        options.add_argument("--ignore-certificate-errors")
        options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
        # Add spaces to separate options initiation and driver initiation for better clarity
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)

    def close(self):
        """Close the WebDriver."""
        self.driver.quit()