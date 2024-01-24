import requests
from bs4 import BeautifulSoup

#URL that's being scraped
ubereats_url = 'https://www.ubereats.com/au/store/mcdonalds-wynyard-railway/Uut2xdbmRViL3VuwXwDSdg?diningMode=DELIVERY'

response = requests.get(ubereats_url)

print('Status Code', response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')

print('Page title:', soup.title.text)