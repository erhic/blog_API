# import urllib.request
# import json
# from .models import Quote

# # function to get quote from API
# def get_quote():
#     response = urllib.request('http://quotes.stormconsultancy.co.uk/random.json')
#     if response.status_code == 200:
#         quote = response.json()
#         print(quote)
#         return quote
import requests

def get_quote():

    r = requests.get('http://quotes.stormconsultancy.co.uk/popular.json')

    r.json()

    return r.json()