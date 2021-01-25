# Web Scraping - Mission to Mars

![mission_to_mars](https://github.com/Chahnaz-Kbaisi/Web-Scraping-Challenge/blob/main/Instructions/Images%20Given/mission_to_mars.png)

A web application was build to scrape various websites for data related to the Mission to Mars and displays the information in a HTML page. The following steps were followed:

## Step 1 - [Scraping](https://github.com/Chahnaz-Kbaisi/Web-Scraping-Mission-to-Mars/blob/main/Missions_to_Mars/Mission_to_Mars.ipynb)

The initial scraping was performed using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

* A Jupyter Notebook file called `mission_to_mars.ipynb` was created and used to complete all of the scraping and analysis tasks. 

### NASA Mars News

* The [NASA Mars News Site](https://mars.nasa.gov/news/) was scraped and collected the latest News Title and Paragraph Text. The text were assign to variables for later reference.

```python
# Example:
news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"

news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."
```
### JPL Mars Space Images - Featured Image

* The url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).

* Splinter was used to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.

* A complete url string for this image was saved.

```python
# Example:
featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'
```
### Mars Facts

* From the Mars Facts webpage [here](https://space-facts.com/mars/) the table containing facts about the planet including Diameter, Mass, etc was scraped using Pandas.

* Pandas was used to convert the data to a HTML table string.

### Mars Hemispheres

* The USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) was visted to obtain high resolution images for each of Mar's hemispheres.

* The full resolution image was obtained by clicking each of the links to the hemispheres in order to find the image url.

* The image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name were saved. A Python dictionary was used to store the data using the keys `img_url` and `title`.

* The dictionary with the image url string and the hemisphere title was appened to a list. This list contained one dictionary for each hemisphere.

```python
# Example:
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    {"title": "Cerberus Hemisphere", "img_url": "..."},
    {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    {"title": "Syrtis Major Hemisphere", "img_url": "..."},
]
```
- - -

## Step 2 - [MongoDB and Flask Application](https://github.com/Chahnaz-Kbaisi/Web-Scraping-Mission-to-Mars/blob/main/Missions_to_Mars/app.py)

MongoDB with Flask templating was used to create a new HTML page that displayed all of the information that was scraped from the URLs above.

* The Jupyter notebook was converted into a Python script called `scrape_mars.py` with a function called `scrape` that executed all of the scraping code from above and return one Python dictionary containing all of the scraped data.

* A route called `/scrape` that will import the `scrape_mars.py` script was created and called `scrape` function.

  * The return value was stored in Mongo as a Python dictionary.

* A root route `/` was created to query the Mongo database and pass the mars data into an HTML template to display the data.

* Create A template [HTML file](https://github.com/Chahnaz-Kbaisi/Web-Scraping-Mission-to-Mars/blob/main/Missions_to_Mars/templates/index.html) called `index.html` was created to hold the mars data dictionary and display all of the data in the appropriate HTML elements. 
- - -

### Copyright

Trilogy Education Services © 2020. All Rights Reserved.
