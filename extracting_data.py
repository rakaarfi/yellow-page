from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from navigating_page import PageNavigator

class DataExtractor:
    """Handles data extraction from the webpage."""
    def __init__(self, driver):
        self.driver = driver
        """
        instead of passing driver as a parameter,
        pass the DriverSetup object instead.

        therefore, you dont need to create WebDriverWait anymore
        """
        self.wait = WebDriverWait(driver, 10)
        self.navigator = PageNavigator(driver)

    def get_text_by_selector(self, selector_type, selector_value):
        try:
            element = self.driver.find_element(selector_type, selector_value)
            return element.text.strip()
        except NoSuchElementException:
            return "N/A"

    def extract_contact_info(self):
        """Extract phone number and website."""
        try:
            """
            bar is too long, try to shorten it. Standard length is 79 characters

            example: 
            xpath = '//*[@id="ypgBody"]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul'
            bar = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(By.XPATH, xpath))
            """
            bar = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ypgBody"]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul')))
            phone_button = bar.find_element(By.CSS_SELECTOR, 'li a')
            phone_button.click()
            phone_number = bar.find_elements(By.XPATH, 'li')[0].find_element(By.CSS_SELECTOR, 'span.mlr__sub-text').text
        except (TimeoutException, NoSuchElementException):
            phone_number = "N/A"

        try:

            website_button = bar.find_elements(By.XPATH, 'li')[-1].find_element(By.TAG_NAME, 'a')
            sub_url = self.driver.current_url
            website_button.click()

            if len(self.driver.window_handles) == 1:
                if sub_url == self.driver.current_url:
                    # Case where no new window is opened
                    website_element = bar.find_elements(By.CSS_SELECTOR, 'li.mlr__submenu__item.mlr__submenu__itemnotprint')
                    website = website_element[0].find_element(By.CSS_SELECTOR, 'span.mlr__sub-text').text if website_element else 'No website found'
            
                else:
                    website = 'No website found'
                    self.navigator.go_back()
            else:
                self.wait.until(lambda d: len(d.window_handles) == 2)
                self.driver.switch_to.window(self.driver.window_handles[1])
                website = self.driver.current_url
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])

        except (TimeoutException, NoSuchElementException):
            website = "N/A"
        
        return phone_number, website