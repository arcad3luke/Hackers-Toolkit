
# Import necessary libraries
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

# Read the input file containing the website URLs and element classes to scrape
input_df = pd.read_csv('GoogleHackMasterList.csv')

# Set up the Chrome driver
s = Service('C:\Program Files\Google\Chrome\Application\chrome.exe')
driver = webdriver.Chrome(service=s)

# Loop through each row in the input file and scrape the necessary data
for index, row in input_df.iterrows():
    website_url = row['Website URL']
    title_class = row['Title Class']
    link_class = row['Link Class']
    description_class = row['Description Class']

    # Navigate to the website to scrape
    driver.get(website_url)

    # Get the page source and parse it with Beautiful Soup
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the elements on the page to scrape
    titles = soup.find_all('h3', class_=title_class)
    links = soup.find_all('a', class_=link_class)
    descriptions = soup.find_all('p', class_=description_class)

    # Create an empty DataFrame to store the scraped data
    df = pd.DataFrame(columns=['Title', 'Link', 'Description'])

    # Loop through the scraped elements and extract the necessary information
    for i in range(len(titles)):
        title = titles[i].text
        link = links[i]['href']
        description = descriptions[i].text

        # Append the information to the DataFrame
        df = df.append({'Title': title, 'Link': link, 'Description': description}, ignore_index=True)

    # Save the scraped data to a CSV file with the website name as the filename
    website_name = website_url.split('//')[1].split('.')[0]
    df.to_csv(f'{website_name}_scraped_data.csv', index=False)

# Close the Chrome driver
driver.quit()