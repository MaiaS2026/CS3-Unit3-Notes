from flask import Flask
from flask import render_template

# Create an instance of Flask
app = Flask(__name__)

# Function that returns content
# using the app.route decorator to map the URL
@app.route("/")
def index(): 
    name_data = 'Maia'
    year_data = 2026
    # Can also use lists & dictionaries
    favorites_list = ['Iced Dunkalatte', 'Iced Latte w/ Sweet Cream Cold Foam', 'Strawberry Acai Lemonade', 'Mango Pineapple Refresher', 'Iced Peach Green Tea']
    ratings_dict = {
                    'Iced Dunkalatte' : 'I rate this drink a 10/10',
                    'Iced Latte w/ Sweet Cream Cold Foam' : 'I rate this drink a 7/10',
                    'Strawberry Acai Lemonade' : 'I rate this drink a 8/10',
                    'Mango Pineapple Refresher' : 'I rate this drink a 9/10',
                    'Iced Peach Green Tea' : 'I rate this drink a 7.5/10'
                    }

    # name is how we refer to it in the HTML template,
    # name_data is the variable declared here in Python
    return render_template("index.html", name=name_data, year=year_data, favorites=favorites_list, ratings = ratings_dict)

# TO RUN YOUR APP - type "flask run" into the TERMINAL
# (if you closed your terminal, open it again with CTRL + `)
# TO STOP click CTRL + C in the TERMINAL