import requests
import pandas as pd

def fetch_economic_indicators():
    API_KEY = 'your_fred_api_key'
    indicators = {
        "leading": "GNPCA",  # Example FRED ID for Gross National Product
        "coincident": "PAYEMS",  # Example FRED ID for Total Nonfarm Payrolls
        "lagging": "CPIAUCSL"  # Example FRED ID for Consumer Price Index
    }
    data_frames = {}
    for key, indicator_id in indicators.items():
        url = f'https://api.stlouisfed.org/fred/series/observations?series_id={indicator_id}&api_key={API_KEY}&file_type=json'
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame(data['observations'])
        data_frames[key] = df
        df.to_csv(f'data/{key}_indicators.csv', index=False)
    return data_frames

if __name__ == "__main__":
    economic_data = fetch_economic_indicators()
    print("Economic indicators ingested successfully.")
