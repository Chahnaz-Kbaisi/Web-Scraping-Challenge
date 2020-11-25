# Dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/mars_database'
mongo = PyMongo(app)


@app.route('/')
def index():

    # Retrieve data into the index & render into the homepage
    mars_database = mongo.db.mars_database.find_one()
    print(mars_database)
    return render_template('index.html', mars_database=mars_database)


@app.route('/scrape')
def scrape():

    # Calling in the function defined in scrape_mars.py
    mars_database = scrape_mars.scrape()
    print(mars_database)
    # Saving into mongodb
    mongo.db.mars_database.update({}, mars_database, upsert=True)

    # return redirect('/')
    return 'DONE!'


if __name__ == "__main__":
    app.run(debug=True)
