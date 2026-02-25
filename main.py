import requests


def main():
    url = "https://api.coingecko.com/api/v3/simple/price"
    crypto = input(
        'Name the crytpo youd like to research? Ex bitcoin,ethereum:').strip().lower()
    params = {
        "ids": crypto,
        "vs_currencies": "usd"
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("error fetching data")
        return

    data = response.json()
    if crypto in data:
        price = data[crypto]["usd"]
        print(f"The price of {crypto} at the moment is: ${price}")
    else:
        print('sorry we do not support that token at the moment')


if __name__ == "__main__":
    main()
