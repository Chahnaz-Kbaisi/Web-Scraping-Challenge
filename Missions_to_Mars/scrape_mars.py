# Converting Jupyter notebook into a Python script:

from splinter import Browser
from bs4 import BeautifulSoup
from splinter.exceptions import ElementDoesNotExist
import pandas as pd


def scrape():
    # MAC
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    # NASA Mars News:
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html

    # Creating BeautifulSoup object from the webpage:
    soup = BeautifulSoup(html, 'html.parser')

    # Collecting the latest news title and paragraph:
    list_object = soup.find('ul', class_="item_list")
    news_title = list_object.find('div', class_="content_title").text
    news_parag = list_object.find('div', class_="article_teaser_body").text

    # JPL Mars Space Images - Featured Image
    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(image_url)

    # For more informatiom go to:
    img_botton = browser.find_by_id('full_image')
    img_botton.click()

    # For more information go to:
    img_url = browser.links.find_by_partial_text('more info')
    img_url.click()

    html = browser.html
    # Creating BeautifulSoup object from the webpage:
    soup_image = BeautifulSoup(html, 'html.parser')

    # Scraping the url for the image object:
    list_image = soup_image.find('figure', class_='lede')
    image_obj = list_image.find('a')['href']

    # Printing image object:
    featured_image_url = f'https://www.jpl.nasa.gov{image_obj}'

    # Mars Facts

    # Using splinter to view Mars Facts webpage:
    url_facts = 'https://space-facts.com/mars/'
    browser.visit(url_facts)
    html = browser.html

    # Using pandas 'read_html' function to automatically scrape the data from the webpage:
    tables = pd.read_html(url_facts)

    # Using normal pandas indexing to slice off dataframes:
    facts_df = tables[0]

    # Renaming dataframe columns:
    facts_df.columns = ['Facts', 'Values']

    # Setting dataframe index:
    mars_fact = facts_df.set_index('Facts', inplace=True)

    # Using Pandas to convert the data to a HTML table string:
    mars_facts = facts_df.to_html('table.html')
