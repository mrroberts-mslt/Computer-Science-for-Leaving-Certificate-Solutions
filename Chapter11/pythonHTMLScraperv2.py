import csv
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
#file = open("scraper.csv", "a")
with open('scraper.csv', 'a', newline='') as csvfile:
    for product in prodElements:
        titleElement = product.find("h4", class_="name")
        title = titleElement.text
        print(title)
    #file.write(title+",")
    
        #csvtitle = csv.writer(csvfile)

        csvtitle = csv.writer(csvfile, delimiter=' ',quotechar='', quoting=csv.QUOTE_MINIMAL)
        csvtitle.writerow(title)
    

csvfile.close()
