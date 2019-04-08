## What is Beautiful Soup?
Beautiful Soup is a Python library for pulling data out of HTML and XML files. It commonly saves programmers hours or days of work.

## Concepts behind Beautiful Soup
When you want to scrape all the links inside of a website, use python's Beautiful Soup library to create a resources page. 4 main objects in Beatiful soup
    1) BeautifulSoup object
    2) Tag object
    3) NavigableString object
    4) Comment object

install 
```python
from bs4 import BeautifulSoup

soup = BeautifulSoup('<b body="description"">Product Description</b>', 'html')
```
  - A link to all relevant resources. This can include the software's site, a helpful tutorial site, a medium article, etc.
  

## Usability Case
We used Beautiful Soup to scrape ingredients from a skincare product on Sephora. First, create an environment and install Beautiful Soup 4:

```$ pip3 install virtualenv
$ virtualenv .env -p python3
$ source .env/bin/activate
$ pip3 install beautifulsoup4 html-parser requests
$ pip3 freeze > requirements.txt```

Then place this code in an app.py file:

```import requests
from bs4 import BeautifulSoup

# Collect and parse first page
page = requests.get('https://www.sephora.com/product/protini-tm-polypeptide-cream-P427421')
soup = BeautifulSoup(page.text, 'html.parser')

# Pull all text from the BodyText div
ingredient_list = soup.find_all('div', class_='css-pz80c5')

ingredientsLength = len(ingredient_list)

print(ingredient_list[ingredientsLength-1].get_text())```

Then run `python3 app.py` to output the skincare product's ingredients to your terminal.

    - Lynda Intro to [Beautiful Soup](https://www.lynda.com/Python-tutorials/Introduction-Beautiful-Soup)
    - [Web scrap](https://www.dataquest.io/blog/web-scraping-tutorial-python/)
    - Medium article on [beautifulsoup](https://medium.com/@wahyudihandry/how-to-build-web-scraping-using-beautifulsoup-and-flask-part-i-ca38a167c236)
    - Official [doc](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
    - [Youtube](https://youtu.be/XQgXKtPSzUI)

