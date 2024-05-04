from datetime import datetime
import requests

def get_stock_prices(symbol, start_date, end_date, api_key):
    # Convert start and end dates to the required format (YYYY-MM-DD)
    start_date_formatted = datetime.strptime(start_date, '%Y-%m-%d').date()
    end_date_formatted = datetime.strptime(end_date, '%Y-%m-%d').date()

    # Construct the API URL with user inputs
    url = f'https://api.polygon.io/v2/aggs/ticker/{symbol}/range/1/day/{start_date_formatted}/{end_date_formatted}?apiKey={api_key}'

    # Make the API request
    response = requests.get(url)
    
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()
        # Extract the results if available
        results = data.get('results')
        if results:
            # Extract required information from results
            stock_prices = []
            for result in results:
                open_price = result.get('o', '-')
                close_price = result.get('c', '-')
                high_price = result.get('h', '-')
                low_price = result.get('l', '-')
                # Format the information
                price_info = f"Open: {open_price}, Close: {close_price}, High: {high_price}, Low: {low_price}"
                stock_prices.append(price_info)
            return stock_prices
        else:
            return None  # No results available
    else:
        return None  # Request failed
