import requests
from bs4 import BeautifulSoup
import pandas as pd

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

# Run the scrape and display results
if __name__ == "__main__":
    df = scrape_data()
    print(df.head())  # Display the first few rows of the DataFrame
