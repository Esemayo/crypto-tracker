import requests
def get_price(coin, currency = "usd"):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": coin,
        "vs_currencies": currency,
        "include_24hr_change": "true"
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        return None, None, "Error"
    data = response.json()
    if coin not in data or currency not in data[coin]: 
        return None, None, "Error"   
    price = data[coin][currency]
    change = data[coin].get(f"{currency}_24h_change") 
    return price, change, None
def main():
    import sys
    print(sys.argv)
    coins = sys.argv[1:]
    if not coins:
        print("Ex Usage: python3 main.py bitcoin solana ethereum ")
        sys.exit()
    currency = "usd"
    print(f'{'Coin':<12}{'Price (USD)':>14}{'24h Change':>12}')
    print("-" * 36)
    #print formats coin_width=12, price_width=14, change_width=12
    for coin in coins:
        price, change, error = get_price(coin, currency)
        if error:
            print("error retrieving data")   
        else:
            print(f'{coin.title():<12}${price:>12,.2f}{change:>+10.2f}%')
if __name__ == "__main__":
    main()
    #main objective single api request
    #side quest edit the dictionary to request all the coins info then return it 
    #sidequest change ccoins list to sys.argv1 to get user input instead of hardcoded list
    #side quest store the information to later use for top gainers/ losers and later on portfolio performance 
    #current status - operational last features added "multi coin lookup and output improvement"
    #last features added "multi coin lookup and formatted output"