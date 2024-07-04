import requests
import pandas as pd

def fetch_etf_data():
    API_KEY = 'your_alpha_vantage_api_key'
    symbol = 'SPY'  # Example ETF symbol
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}'
    
    response = requests.get(url)
    data = response.json()
    
    # Parse the JSON data into a DataFrame
    time_series = data['Time Series (Daily)']
    df = pd.DataFrame.from_dict(time_series, orient='index')
    df.reset_index(inplace=True)
    df.columns = ['date', 'open', 'high', 'low', 'close', 'volume']
    
    return df

if __name__ == "__main__":
    etf_df = fetch_etf_data()
    etf_df.to_csv('data/etfs.csv', index=False)
    print("ETF data ingested successfully.")
