from scraping.collecting_data import DataCollector


def parsing(save_as):
    # Initialize objects
    data_collector = DataCollector()

    # Define URL and open it
    url = 'https://www.yellowpages.ca/search/si/1/Dentists/Toronto+ON'
    data_collector.collect_data(url)

    # Export data to Excel
    data_collector.to_excel(save_as)
