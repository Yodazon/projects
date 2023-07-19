import requests
from bs4 import BeautifulSoup

url = "https://www.ticketmaster.ca/bad-omens-toronto-ontario-09-19-2023"
response = requests.get(url)


soup = BeautifulSoup(response.content, "html.parser")
prices = soup.find_all("span", class_="ticket-price")


ticket_prices = []
for price in prices:
    ticket_prices.append(price.text)

for price in ticket_prices:
    print(price)

