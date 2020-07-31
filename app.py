
import os

import h5py
import tensorflow as tf
from tensorflow import keras
# from tensorflow.keras.preprocessing.text import Tokenizer
# import tensorflow as tf
# from tensorflow import keras
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# import pandas as pd
# import numpy as np
# from tensorflow.keras.preprocessing.sequence import pad_sequences

from flask import Flask, jsonify, render_template, request, redirect
# import get_data

# import psycopg2

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

app._static_folder = 'static/'

##################################

# # Connects to the database using the app config


#################################################
# Flask Routes
#################################################

new_model = tf.keras.models.load_model('D:/Users/Goutham/Documents/BOOTCAMP/76_64.h5')

padded = [[   2,    1,    1,    7, 2910,   38, 2792,    1, 2629,    1,   12,           2, 2982,    1, 1052,   42,    1,  113,    5,    1,    2, 2105,         818,   28, 2629,    1,    1, 3228]]


####################
#test funct

def test_func():
    return "test_funct_str"

new_model = tf.keras.models.load_model('D:/Users/Goutham/Documents/BOOTCAMP/76_64.h5')

####################



@app.route("/")
def welcome():

    test4 = str(new_model.predict(padded))
    
    test3 = test_func()
    # return render_template("index.html")
    return test4

@app.route('/', methods=['POST'])
def welcome_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text

@app.route("/index.html")
def index():

    return render_template("index.html")

@app.route("/about.html")
def about():

    return render_template("about.html")
    
@app.route("/about2.html")
def about2():

    return render_template("about2.html")

@app.route("/tweetchecker.html")
def tweetchecker():

    return render_template("tweetchecker.html")

if __name__ == '__main__':
    app.run(debug=True)
