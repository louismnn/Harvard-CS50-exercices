import sys
import requests

def main(number):

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        res = response.json()
        price = res["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        sys.exit()

    try:
        worth = float(number) * float(price)
        p = round(worth, 4)
        sys.exit(1,f"${p:,}")

    except ValueError:
        sys.exit("Command-line argument is not a number")

try:
    command = sys.argv[1]
except IndexError:
    sys.exit("Missing command-line argument")

main(command)

