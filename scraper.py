import requests
from bs4 import BeautifulSoup

#URL that's being scraped
ubereats_url = 'https://www.ubereats.com/au/store/mcdonalds-wynyard-railway/Uut2xdbmRViL3VuwXwDSdg?diningMode=DELIVERY'

#Fetch URL response
response = requests.get(ubereats_url)

#Parse HTML content with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

#Find all menu item divs
menu_divs = soup.find_all('div', class_= "al am bz ae ak i7")

#Output
print('Status Code', response.status_code)
print('Page title:', soup.title.text)
print(f"Found {len(menu_divs)} menu items")