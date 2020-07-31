# import numpy as np
import os
# import pandas as pd

from flask import Flask, jsonify, render_template, request, redirect
# import get_data


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

app._static_folder = 'static/'

##################################

# # Connects to the database using the app config

#################################################

new_model = tf.keras.models.load_model('76_64.h5')

padded = [[   2,    1,    1,    7, 2910,   38, 2792,    1, 2629,    1,   12,           2, 2982,    1, 1052,   42,    1,  113,    5,    1,    2, 2105,         818,   28, 2629,    1,    1, 3228]]

# print(new_model.predict(padded))
#################################################



#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    
    test4 = str(new_model.predict(padded))
    
    test3 = test_func()
    # return render_template("index.html")
    return test4

@app.route("/index.html")
def index():

    return render_template("index.html")

@app.route("/about.html")
def about():

    return render_template("about.html")
    
@app.route("/about2.html")
def about2():

    return render_template("about2.html")

if __name__ == '__main__':
    app.run(debug=True)
