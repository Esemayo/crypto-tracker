import requests
def get_price(coin, currency):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": coin,
        "vs_currencies": currency,
    }
    response = requests.get(url, params=params)
    data = response.json()
    if response.status_code != 200:
        return None, "error"
    data = response.json()
    if coin not in data or currency not in data[coin]: 
        return None, "Error"  
        
    price = data[coin][currency]
    return price, None

def main():
    crypto = input('Name the crypto youd like to research? Ex bitcoin,ethereum:').strip().lower()
    currency = input("Which currency would you like price to be calculated?").strip().lower()
    price, error = get_price(crypto, currency)
    if error:
        print(error)
    else:
        print(f"The price of {crypto} at the moment is: ${price}")

if __name__ == "__main__":
    main()
