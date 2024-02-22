import sys
import requests


try:
    user_guess = float(input("Enter Expected Price of Bitcoin in USD: "))
except ValueError as err:
    print(err)
    sys.exit(0)
else:
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url)
    data = response.json()
    rate = data['bpi']['USD']
    bitcoin_price = rate['rate']
    bitcoin_price = float(bitcoin_price.replace(',', ''))
    # print(type(bitcoin_price))
    if user_guess > bitcoin_price:
        print("You thought of much higher price")
    elif user_guess < bitcoin_price:
        print("You underestimated Bitcoin!")
    else:
        print("How can you be so accurate?, Did you googled the rate?")
    print(f"The current Bitcoin price is {bitcoin_price} USD")
