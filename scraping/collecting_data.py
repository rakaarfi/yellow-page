import pandas as pd

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class DataCollector:
    """Handles the collection of data from listings."""
    
    def __init__(self, driver_setup, page_navigator, data_extractor):
        self.driver = driver_setup.driver
        self.navigator = page_navigator
        self.extractor = data_extractor
        self.data = {
            "URL": [], "Title": [], "Full Address": [], "Street Address": [],
            "Address Locality": [], "Address Region": [], "Postal Code": [],
            "Phone Number": [], "Website": []
        }

    def collect_data(self, url):
        """Collects data from the specified URL with a limit on the number of listings."""
        self.navigator.open_url(url)
        try:
            # Wait for the element that contains all the links to listings
            links_element = self.navigator.wait_for_element(
                By.CSS_SELECTOR, 'div.resultList.jsResultsList.jsMLRContainer')

            # Find all the links to individual listings
            websites = links_element.find_elements(
                By.CSS_SELECTOR, 'a.listing__name--link.listing__link.jsListingName')
            
            # Extract the URLs from the links
            all_links = [website.get_attribute('href') for website in websites]

            for link in all_links[:3]:
                # Navigate to the details page
                self.navigator.open_url(link)

                # Collect data on the details page
                self.data["URL"].append(self.driver.current_url)

                title_css = 'h1.merchantInfo-title.merchant__title span[itemprop="name"]'
                self.data["Title"].append(
                    self.extractor.get_text_by_selector(By.CSS_SELECTOR, title_css))
                
                full_address_css = 'div.merchant__details__section.merchant__details__section--address'
                self.data["Full Address"].append(
                    self.extractor.get_text_by_selector(By.CSS_SELECTOR, full_address_css))
                
                street_address_css = 'span[itemprop="streetAddress"]'
                self.data["Street Address"].append(
                    self.extractor.get_text_by_selector(By.CSS_SELECTOR, street_address_css))
                
                address_locality_css = 'span[itemprop="addressLocality"]'
                self.data["Address Locality"].append(
                    self.extractor.get_text_by_selector(By.CSS_SELECTOR, address_locality_css))
                
                address_region_css = 'span[itemprop="addressRegion"]'
                self.data["Address Region"].append(
                    self.extractor.get_text_by_selector(By.CSS_SELECTOR, address_region_css))
                
                postal_code_css = 'span[itemprop="postalCode"]'
                self.data["Postal Code"].append(
                    self.extractor.get_text_by_selector(By.CSS_SELECTOR, postal_code_css))

                phone, website = self.extractor.extract_contact_info()
                self.data["Phone Number"].append(phone)
                self.data["Website"].append(website)
        
        except TimeoutException:
            print("Timeout occurred during data collection.")

    def to_excel(self, file_name):
        """Exports the collected data to an Excel file."""
        df = pd.DataFrame(self.data)
        df.to_excel(file_name, index=False)
