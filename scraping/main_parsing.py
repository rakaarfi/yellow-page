from scraping.setup_driver import DriverSetup
from scraping.navigating_page import PageNavigator
from scraping.collecting_data import DataCollector
from scraping.extracting_data import DataExtractor


def parsing(save_as):
    # Initialize objects
    driver_setup = DriverSetup()
    page_navigator = PageNavigator(driver_setup)
    data_extractor = DataExtractor(driver_setup, page_navigator)
    data_collector = DataCollector(driver_setup, page_navigator, data_extractor)

    # Define URL and open it
    url = 'https://www.yellowpages.ca/search/si/1/Dentists/Toronto+ON'
    data_collector.collect_data(url)

    # Export data to Excel
    data_collector.to_excel(save_as)

    driver_setup.close()
