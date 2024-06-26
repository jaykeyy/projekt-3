"""
projekt_3.py: třetí projekt  
author: jakubkapl 
email: kapl@gmail.com 
discord: jakubr#4490 
"""

import sys
import requests
import pandas as pd
from bs4 import BeautifulSoup

def scrape_election_results(url, output_file):
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the URL. Status code:", response.status_code)
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Assuming the data is in a table; adjust selectors based on the actual HTML structure
    data = []
    table = soup.find('table')  # Adjust the selector based on the actual HTML
    rows = table.find_all('tr')

    for row in rows[1:]:  # Skip the header row
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append(cols)

    # Convert to DataFrame
    df = pd.DataFrame(data, columns=['kód obce', 'název obce', 'voliči v seznamu', 'vydané obálky', 'platné hlasy', 'strana_A', 'strana_B'])  # Adjust column names

    # Save to CSV
    df.to_csv(output_file, index=False)
    print(f"Data successfully saved to {output_file}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python projekt_4.py <url> <output_file>")
        return

    url = sys.argv[1]
    output_file = sys.argv[2]

    scrape_election_results(url, output_file)

if __name__ == "__main__":
    main()
