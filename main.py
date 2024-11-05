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
"""
(OPTIONAL)
Add argument to export data based on user input
Example: 

python main.py --save_as <filename>
"""


driver_setup.close()

"""
restructure file for better readability
example:
-------------------------------
main.py
requirements.txt
src/....(put all files here)
-------------------------------

or more modular:
-------------------------------
main.py
requirements.txt
crawler/... (for scraping code)
data_management/...(for data handling code)
-------------------------------

in this main.py file:

define main() and call it

if __name__ == "__main__":
    main()
"""


"""
Add Readme for project explanation with video record or screenshot
Using chatGPT is ok
"""