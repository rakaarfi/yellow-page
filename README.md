# Yellow Pages Dentist Data Scraper
This repository contains a web scraper built to collect detailed information about dentists listed on Yellow Pages for Toronto, ON. The tool scrapes data such as business name, address, phone number, and website URL, saving the output in an Excel file..

## Table of Contents
- [Features](#Features)
- [Project Structure](#Project-Structure)
- [Requirements](#Requirements)
- [Usage](#Usage)
- [Customization](#Customization)
- [Copyright](#Copyright)
  
## Features
- Scrapes dentist information from Yellow Pages.
- Extracts data fields including URL, Title, Address details, Phone Number, and Website.
- Exports data to an Excel file for easy access and analysis.
  
## Project Structure
- **main.py**: Entry point for running the scraper. Configures command-line arguments and initiates the scraping process.
- **main_parsing.py**: Coordinates the main scraping workflow, initializing classes and handling navigation, data collection, and saving.
- **setup_driver.py**: Configures the Selenium WebDriver with options to improve speed and handle browser settings.
- **wait_driver.py**: Manages wait times to ensure elements are loaded before interacting with them.
- **navigating_page.py**: Handles page navigation tasks such as URL loading and element clicks.
- **collecting_data.py**: Structures and stores the extracted data, handling data fields like Title, Address, Phone, and Website.
- **extracting_data.py**: Extracts specific data fields using CSS and XPath selectors, including contact information.

## Requirements
- Python 3.x
- [Selenium WebDriver](https://www.selenium.dev/)
- Chrome browser and ChromeDriver
  
Install dependencies using:
```
pip install -r requirements.txt
```
> Note: Ensure that the correct version of ChromeDriver is installed for your Chrome version.

## Usage
To run the scraper and save the data to an Excel file, use:
```
python main.py --save_as "output_file.xlsx"
```
- `--save_as` (optional): Specifies the name of the output Excel file. Defaults to `dentists_data.xlsx` if not provided.
### Example
```
python main.py --save_as "toronto_dentists.xlsx"
```
This will start the scraper and save the results in an Excel file named `toronto_dentists.xlsx`.

## Customization
- **Target URL**: You can modify the URL in `main_parsing.py` to scrape data for different categories or locations.
- **Data Fields**: Update fields or add new ones in `collecting_data.py` if you need additional details from the listings.

## Copyright
Copyright©2024 ***Raka Arfi***

Released under MIT License
