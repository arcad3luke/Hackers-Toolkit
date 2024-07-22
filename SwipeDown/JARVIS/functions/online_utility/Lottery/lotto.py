import requests
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


def fetch_powerball_statistics(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table')
    rows = table.find_all('tr') if table else []

    data = []
    headers = [th.text.strip() for th in rows[0].find_all('th')]
    print(f"Headers: {headers}")

    for row in rows[1:]:  # Skip header row
        cols = row.find_all('td')
        draw_data = [col.text.strip() for col in cols]
        data.append(draw_data)

    # Print the first row to inspect the structure
    print(f"First row of data: {data[0]}")

    # Update columns based on the actual structure
    columns = headers  # Use the actual headers from the table
    df = pd.DataFrame(data, columns=columns[:len(data[0])])  # Only take the number of columns present in data
    print(f"Columns in dataframe: {df.columns}")

    # Convert the table to long format for analysis
    df_long = df.melt(id_vars=[columns[0]], var_name="Date", value_name="Frequency")
    df_long = df_long.rename(columns={columns[0]: "Number"})
    df_long['Number'] = df_long['Number'].astype(int)
    df_long['Frequency'] = df_long['Frequency'].astype(int)

    return df_long


def exploratory_data_analysis(df, title):
    if df.empty:
        print(f"No data available for {title}.")
        return

    # Aggregate data by number
    df_agg = df.groupby('Number').sum().reset_index()

    # Plot the frequency distribution
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Number', y='Frequency', data=df_agg)
    plt.xlabel('Number')
    plt.ylabel('Frequency')
    plt.title(f'Frequency of {title} Numbers')
    plt.xticks(rotation=90)
    plt.show()


def main():
    # Fetch and preprocess data
    powerball_url = 'https://www.powerball.net/statistics'
    powerball_df = fetch_powerball_statistics(powerball_url)

    if not powerball_df.empty:
        # Exploratory Data Analysis
        exploratory_data_analysis(powerball_df, 'Powerball')

        print(powerball_df.head())
    else:
        print("No data available to analyze.")


if __name__ == "__main__":
    main()
