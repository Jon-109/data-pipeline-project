#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3

def scrape_data():
    # Define the URL to scrape
    url = 'http://quotes.toscrape.com'
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes_data = []
        # Find all quote elements
        quotes = soup.find_all('div', class_='quote')
        for quote in quotes:
            text = quote.find('span', class_='text').get_text()
            author = quote.find('small', class_='author').get_text()
            quotes_data.append({'text': text, 'author': author})
        # Convert to DataFrame
        return pd.DataFrame(quotes_data)
    else:
        print("Failed to retrieve data")
        return pd.DataFrame()

def clean_data(df):
    # Example: Remove quotation marks around the text
    df['text'] = df['text'].str.replace('“', '').replace('”', '')
    # Strip extra whitespace from the author names
    df['author'] = df['author'].str.strip()
    return df

def save_to_database(df, db_name="quotes.db"):
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect(db_name)
    # Save the DataFrame to a SQL table named "quotes"
    df.to_sql('quotes', conn, if_exists='replace', index=False)
    # Close the connection
    conn.close()
    print(f"Data saved to {db_name}")

if __name__ == "__main__":
    df = scrape_data()
    df = clean_data(df)
    save_to_database(df)  # Save the cleaned data to the database
    print(df.head())  # Display the first few rows of the DataFrame