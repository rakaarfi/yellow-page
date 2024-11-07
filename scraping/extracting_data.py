from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class DataExtractor:
    """Handles data extraction from the webpage."""
    def __init__(self, driver_setup, page_navigator):
        self.driver = driver_setup.driver
        self.wait = driver_setup.wait
        self.navigator = page_navigator

    def get_text_by_selector(self, selector_type, selector_value):
        try:
            element = self.driver.find_element(selector_type, selector_value)
            return element.text.strip()
        except NoSuchElementException:
            return "N/A"

    def extract_contact_info(self):
        """Extract phone number and website."""
        try:
            # Wait until the bar is visible
            bar_xpath = '//*[@id="ypgBody"]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul'
            bar = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, bar_xpath)))
            
            # Find the phone number button and click it
            phone_button = bar.find_element(By.CSS_SELECTOR, 'li a')
            phone_button.click()

            # Get the text of the phone number
            phone_number_element = bar.find_elements(By.XPATH, 'li')[0]
            phone_number = phone_number_element.find_element(
                By.CSS_SELECTOR, 'span.mlr__sub-text').text
            
        except (TimeoutException, NoSuchElementException):
            phone_number = "N/A"

        try:

            # Find the website button
            website_button = bar.find_elements(By.XPATH, 'li')[-1].find_element(By.TAG_NAME, 'a')
            # Get the current URL before clicking the button for later comparison
            sub_url = self.driver.current_url
            # Click the website button
            website_button.click()

            if len(self.driver.window_handles) == 1:
                if sub_url == self.driver.current_url:
                    # Case where no new window is opened
                    website_element = bar.find_elements(
                        By.CSS_SELECTOR, 'li.mlr__submenu__item.mlr__submenu__itemnotprint')
                    
                    website = (website_element[0].find_element(By.CSS_SELECTOR, 'span.mlr__sub-text').text 
                        if website_element else 'No website found')
            
                else:
                    website = 'No website found'
                    self.navigator.go_back()
            else:
                # Case where new window is opened                
                self.wait.until(lambda d: len(d.window_handles) == 2) # Wait until the new window is opened                
                self.driver.switch_to.window(self.driver.window_handles[1]) # Switch to the new window

                # Get the URL of the new window
                website = self.driver.current_url

                # Switch back to the first window
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])

        except (TimeoutException, NoSuchElementException):
            website = "N/A"
        
        return phone_number, website
