# Dentist Data Scraper
This repository contains a web scraper built to extract data about dentists from the Yellow Pages website for Toronto, ON. The tool collects information such as the business name, address, phone number, and website link, and saves the data in an Excel file.

## Table of Contents
- [Features](#Features)
- [Project Structure](#Project-Structure)
- [Requirements](#Requirements)
- [Usage](#Usage)
- [Customization](#Customization)
- [Copyright](#Copyright)
  
## Features
- Scrapes dentist listings from Yellow Pages.
- Extracts essential details including URL, Title, Full Address, Phone Number, and Website.
- Exports the collected data to an Excel file for easy data management.
  
## Project Structure
- **main.py**: Entry point for running the scraper. Configures and initiates the scraping process.
- **main_parsing.py**: Manages the main scraping flow, initializing necessary classes and starting the data collection process.
- **setup_driver.py**: Sets up the Selenium WebDriver for Chrome, including options for window maximization and image loading preferences to optimize scraping.
- **navigating_page.py**: Handles navigation on the website, including URL loading and element interaction.
- **collecting_data.py**: Collects data from each listing on the Yellow Pages site, such as address, phone, and website.
- **extracting_data.py**: Extracts specific data fields using CSS and XPath selectors, including handling contact information with multiple steps for data extraction.

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
python main.py --save_as "dentists_info.xlsx"
```
This will start the scraper and save the results in an Excel file named `dentists_info.xlsx`.

## Customization
- Target URL: You can modify the URL to scrape a different category or location by updating the URL in `main_parsing.py`.
- Data Fields: Modify fields or add new ones in `collecting_data.py` if you want to extract additional information from the listings.

## Copyright
Copyright©2024 Raka Arfi

Released under MIT License
