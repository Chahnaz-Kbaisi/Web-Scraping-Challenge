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

    # Mars Hemispheres

    # The URL page to be scraped using splinter:
    url_hemispheres = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url_hemispheres)

    html = browser.html
    # Creating BeautifulSoup object from the webpage:
    soup_obj = BeautifulSoup(html, "html.parser")

    items = soup_obj.find_all('div', class_="item")
    hemisphere_title = soup_obj.find_all('div', class_="description")

    # Use a Python dictionary to store the data using the keys img_url and title.
    hemispheres_urls_dict = []

    # Starting a loop to collect title and img_url:
    items = soup_obj.find_all('div', class_="item")

    # The main url for the webpage:
    main_url = 'https://astrogeology.usgs.gov'

    # Looping through for all the information:
    for item in items:
        # Locating & storing the titles:
        title = item.find("h3").text
        # print(title)

        # Locating & storing the link
        img_link = item.find("a", class_="itemLink product-item")["href"]
        # print(img_link)

        # Storing the url using browser:
        browser.visit(main_url + img_link)

        # HTML object:
        img_link_html = browser.html

        # Collecting full image url:
        img_url = main_url + soup_obj.find('img', class_='thumb')['src']

        hemispheres_urls_dict.append({"title": title, "img_url": img_url})

        browser.quit()

        # Storing the dataset into dictionary:

        mars_database = {
            "news_title": news_title,
            "news_paragraph": news_parag,
            "featured_image_url ":  featured_image_url,
            "mars_facts": mars_facts,
            "hemispheres_images_urls": hemispheres_urls_dict
        }

        return mars_database
