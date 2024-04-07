import requests
from bs4 import BeautifulSoup

# URL of the page you want to scrape
url = 'https://app.v1.statusplus.net/membership/provider/index?society=ipps'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

print(soup)

# Find all elements containing names and addresses
address_containers = soup.find_all('div', class_='address-container')

# Extract names and addresses and print
for container in address_containers:
    name = container.find('h4').text.strip()
    address = container.find('address').text.strip().replace('\n', ' ')
    print("Name:", name)
    print("Address:", address)
    print()

