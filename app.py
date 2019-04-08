import requests
from bs4 import BeautifulSoup

# Collect and parse first page
page = requests.get('https://www.sephora.com/product/protini-tm-polypeptide-cream-P427421?icid2=bestsellerskincare_us_skugrid_ufe:p427421:product')
soup = BeautifulSoup(page.text, 'html.parser')

# Pull all text from the BodyText div
ingredient_list = soup.find_all('div', class_='css-pz80c5')

ingredientsLength = len(ingredient_list)

print(ingredient_list[ingredientsLength-1].get_text())