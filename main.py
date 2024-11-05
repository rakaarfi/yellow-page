from setup_driver import DriverSetup
from exporting_data import DataExporter
from collecting_data import DataCollector

# Main execution
driver_setup = DriverSetup()
data_collector = DataCollector(driver_setup.driver)

# Define URL and open it
url = 'https://www.yellowpages.ca/search/si/1/Dentists/Toronto+ON'
data_collector.collect_data(url)

# Export data using DataExporter
exporter = DataExporter(data_collector.data)
exporter.to_excel('dentists_data.xlsx')

driver_setup.close()