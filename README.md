# Data Pipeline Automation Project

This project is an automated data pipeline built to scrape, clean, and store data from the web. The pipeline is designed to run daily, collecting quotes and authors from a sample website, cleaning the data, and storing it in a SQLite database. 

The project utilizes Python, SQLite, and a cron job for automation, making it a powerful example of combining web scraping, data processing, and task scheduling.

## Project Overview

- **Goal**: Automate the collection of data from a website, clean it, and save it for analysis or future use.
- **Data Source**: [Quotes to Scrape](http://quotes.toscrape.com) - a sample website commonly used for web scraping practice.
- **Automation**: A cron job is scheduled to run the script daily at midnight, ensuring that the data is always up-to-date.

## Skills Developed

- **Web Scraping**: Extracting data from websites using Python's `requests` and `BeautifulSoup` libraries.
- **Data Cleaning**: Standardizing and cleaning text data with `pandas` to ensure consistency.
- **Database Management**: Using `sqlite3` to store scraped data in a structured format.
- **Automation**: Scheduling automated tasks with cron jobs to run the script daily without manual intervention.
- **Version Control**: Tracking project changes with Git and GitHub.

## Tools and Platforms

- **Python**: Core programming language used for all stages of the pipeline.
- **Libraries**:
  - `requests`: For making HTTP requests and retrieving HTML content.
  - `beautifulsoup4`: For parsing and extracting data from HTML.
  - `pandas`: For cleaning and structuring data.
  - `sqlite3`: Python’s built-in library for interacting with SQLite databases.
- **SQLite**: A lightweight database to store and organize data locally.
- **Git and GitHub**: Version control to track code changes and maintain an accessible online repository.
- **Cron (macOS)**: A task scheduler to run the script automatically at specified times.

## Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YourUsername/data-pipeline-project.git
cd data-pipeline-project
