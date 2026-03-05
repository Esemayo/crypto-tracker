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
        return None, "Error"
    data = response.json()
    if coin not in data or currency not in data[coin]: 
        return None, "Error"   
    price = data[coin][currency]
    change = data[coin].get(f"{currency}_24h_change") 
    return price, change, None
def main():
    coins = ["bitcoin", "bittensor", "kaspa"]
    currency = "usd"
    print(f'{'Coin':<12}{'Price (USD)':>14}{'24h Change':>12}')
    print("-" * 36)
    for coin in coins:
        price, change, error = get_price(coin, currency)
        if error:
            print(error)   
        else:
            print(f'{coin.title():<12}${price:>12,.2f}{change:>+10.2f}%')
if __name__ == "__main__":
    main()
    #main objective multi coin dashboard refactor
    #side quest create a loop to get a lookup of Bittenor, Kaspa, Bitcoin(hint- for coin in results:)
    #side quest we need to figure out how to expand the dictionary for the data of the new coins
    #hint for dictionary instead of expasion- results[coin] = {"price": price, "change": change}
    #side quest improve out put to show the coin price and change in a neat table 
    #current status - 
    