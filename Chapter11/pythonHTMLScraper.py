import requests
from bs4 import BeautifulSoup

URL = "https://www.novatel.ie/mobile-phone-signal-repeater-kits"
URL2 = "https://www.novatel.ie/mobile-phone-signal-booster-kits-for-homes"
URL3 ="https://www.novatel.ie/mobile-phone-signal-booster-kits-for-offices"
URL4 = "https://www.novatel.ie/marine-signal-repeaters"
URL5 = "https://www.novatel.ie/in-vehicle-signal-repeaters"



page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="content")

prodElements = results.find_all("div", class_="product-grid-item")

# titles = soup.find_all("h4", class_="name")

for product in prodElements:
    titleElement = product.find("h4", class_="name")
    print(titleElement.text)
#     prodDesc = product.find("p", class_="description")
#     print(prodDesc.text)





#productName = results.find_all("div", class_="caption")



#print(page.content)
