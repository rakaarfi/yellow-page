from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from extracting_data import DataExtractor
from navigating_page import PageNavigator

class DataCollector:
    """Handles the collection of data from listings."""
    
    def __init__(self, driver):
        self.driver = driver
        self.navigator = PageNavigator(driver)
        self.extractor = DataExtractor(driver)
        self.data = {
            "URL": [], "Title": [], "Full Address": [], "Street Address": [],
            "Address Locality": [], "Address Region": [], "Postal Code": [],
            "Phone Number": [], "Website": []
        }

    def collect_data(self, url):
        """Collects data from the specified URL with a limit on the number of listings."""
        self.navigator.open_url(url)
        try:
            links_element = self.navigator.wait_for_element(By.CSS_SELECTOR, 'div.resultList.jsResultsList.jsMLRContainer')
            links = links_element.find_elements(By.CSS_SELECTOR, 'div.listing.listing--bottomcta')

            for link in links:
                link_button = link.find_element(By.CSS_SELECTOR, 'a.listing__name--link.listing__link.jsListingName')
                self.navigator.click_element(link_button)

                # Collect data on the details page
                self.data["URL"].append(self.driver.current_url)
                self.data["Title"].append(self.extractor.get_text_by_selector(By.CSS_SELECTOR, 'h1.merchantInfo-title.merchant__title span[itemprop="name"]'))
                self.data["Full Address"].append(self.extractor.get_text_by_selector(By.CSS_SELECTOR, 'div.merchant__details__section.merchant__details__section--address'))
                self.data["Street Address"].append(self.extractor.get_text_by_selector(By.CSS_SELECTOR, 'span[itemprop="streetAddress"]'))
                self.data["Address Locality"].append(self.extractor.get_text_by_selector(By.CSS_SELECTOR, 'span[itemprop="addressLocality"]'))
                self.data["Address Region"].append(self.extractor.get_text_by_selector(By.CSS_SELECTOR, 'span[itemprop="addressRegion"]'))
                self.data["Postal Code"].append(self.extractor.get_text_by_selector(By.CSS_SELECTOR, 'span[itemprop="postalCode"]'))

                phone, website = self.extractor.extract_contact_info()
                self.data["Phone Number"].append(phone)
                self.data["Website"].append(website)

                # Go back to the main listings page
                self.navigator.go_back()
                self.navigator.wait_for_element(By.CSS_SELECTOR, 'div.resultList.jsResultsList.jsMLRContainer')
        
        except TimeoutException:
            print("Timeout occurred during data collection.")