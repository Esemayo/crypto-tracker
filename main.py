import requests
def get_price(coin, currency):
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
    crypto = input('Name the crypto youd like to research? Ex bitcoin,ethereum:').strip().lower()
    currency = input("Which currency would you like price to be calculated?").strip().lower()
    price, change, error = get_price(crypto, currency)
    if error:
        print(error)
    if change is not None:
        print(f"The price of {crypto} at the moment is: {price:,.2f} 24hr change is :{change:.2f} %")
    else:
        print(f"The price of {crypto} at the moment is: {price:,.2f} 24hr change is :N/A")
if __name__ == "__main__":
    main()
    #main objective multi coin dashboard refactor
    #side quest improve out put to show the coin price and change in a neat table 
    #current status - operational
    #