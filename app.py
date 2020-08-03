import numpy as np
import os
import pandas as pd
import h5py
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
import tweet_scrape
import tweet_clean_tokenizer

# from tensorflow.keras.preprocessing.text import Tokenizer
# import tensorflow as tf
# from tensorflow import keras
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# import pandas as pd
# import numpy as np
# from tensorflow.keras.preprocessing.sequence import pad_sequences

from flask import Flask, jsonify, render_template, request, redirect, url_for
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
ap_tweet_list = tweet_scrape.AP_tweet("AP")

new_model = tf.keras.models.load_model('D:/Users/Goutham/Documents/BOOTCAMP/76_64.h5')

padded = [[   2,    1,    1,    7, 2910,   38, 2792,    1, 2629,    1,   12,           2, 2982,    1, 1052,   42,    1,  113,    5,    1,    2, 2105,         818,   28, 2629,    1,    1, 3228]]

def tweet_full(text):
    cleaned_test_tweet = tweet_clean_tokenizer.tweet_cleaner(text)
    tokenized_test_tweet = tweet_clean_tokenizer.tweet_tokenizer(cleaned_test_tweet)
    dis_perc = new_model.predict(tokenized_test_tweet)
    if dis_perc >= 0.5:
        dis_des = "DISASTER"
    else:
        dis_des = "NOT A DISASTER"
    
    return [dis_perc,dis_des,cleaned_test_tweet]


ap1, ap2, ap3, ap4, ap5, ap6, ap7, ap8, ap9, ap10, ap11, ap12, ap13, ap14, ap15, ap16, ap17, ap18, ap19, ap20 = ap_tweet_list[1][0], ap_tweet_list[1][1], ap_tweet_list[1][2], ap_tweet_list[1][3], ap_tweet_list[1][4], ap_tweet_list[1][5], ap_tweet_list[1][6], ap_tweet_list[1][7], ap_tweet_list[1][8], ap_tweet_list[1][9], ap_tweet_list[1][10], ap_tweet_list[1][11], ap_tweet_list[1][12], ap_tweet_list[1][13], ap_tweet_list[1][14], ap_tweet_list[1][15], ap_tweet_list[1][16], ap_tweet_list[1][17], ap_tweet_list[1][18], ap_tweet_list[1][19]
ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8, ch9, ch10, ch11, ch12, ch13, ch14, ch15, ch16, ch17, ch18, ch19, ch20 = tweet_full(ap_tweet_list[0][0]), tweet_full(ap_tweet_list[0][1]), tweet_full(ap_tweet_list[0][2]), tweet_full(ap_tweet_list[0][3]), tweet_full(ap_tweet_list[0][4]), tweet_full(ap_tweet_list[0][5]), tweet_full(ap_tweet_list[0][6]), tweet_full(ap_tweet_list[0][7]), tweet_full(ap_tweet_list[0][8]), tweet_full(ap_tweet_list[0][9]), tweet_full(ap_tweet_list[0][10]), tweet_full(ap_tweet_list[0][11]), tweet_full(ap_tweet_list[0][12]), tweet_full(ap_tweet_list[0][13]), tweet_full(ap_tweet_list[0][14]), tweet_full(ap_tweet_list[0][15]), tweet_full(ap_tweet_list[0][16]), tweet_full(ap_tweet_list[0][17]), tweet_full(ap_tweet_list[0][18]), tweet_full(ap_tweet_list[0][19])
####################
#test funct

def test_func():
    return "test_funct_str"

# new_model = tf.keras.models.load_model('D:/Users/Goutham/Documents/BOOTCAMP/76_64.h5')

####################


# test_tweet = ap_tweet_list[0][0]


# for item in ap_tweet_list[0]:
#     cleaned_test_tweet = tweet_clean_tokenizer.tweet_cleaner(item)
#     tokenized_test_tweet = tweet_clean_tokenizer.tweet_tokenizer(cleaned_test_tweet)
#     print(tokenized_test_tweet)
#     print(padded)
#     test4 = str(new_model.predict(tokenized_test_tweet))
#     print(test4)
# print(AP_tweetListOf6)



# print(tweet_full("The Oprah Magazine is ending its regular monthly print editions with the December 2020 issue after 20 years of publication. The announcement comes as print advertising shrinks further amid the pandemic."))




# ap1 = 1288935356310552576
# ap2 = 1287824348460593154
# ap6 = 1289422130485104640

# @app.route("/")
# def welcome():

#     sentence = ["The Oprah Magazine is ending its regular monthly print editions with the December 2020 issue after 20 years of publication. The announcement comes as print advertising shrinks further amid the pandemic."]

#     # sequences = tokenizer.texts_to_sequences(sentence)

#     # padded = pad_sequences(sequences, maxlen= max_length, padding = 'post', truncating= 'post' )

#     # print(model.predict(padded))

#     test4 = str(new_model.predict(padded))
    
#     test3 = test_func()
#     # return render_template("index.html")
#     return test3

@app.route("/test.html")
def test():
    
    return "AP_123"

@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        try:
            user = request.form["nm"]
        except:
            user = "reuters"

        # userInput = tweet_scrape.AP_tweet("reuters")
        ap_tweet_list = tweet_scrape.AP_tweet(user)
        

        ap1, ap2, ap3, ap4, ap5, ap6, ap7, ap8, ap9, ap10, ap11, ap12, ap13, ap14, ap15, ap16, ap17, ap18, ap19, ap20 = ap_tweet_list[1][0], ap_tweet_list[1][1], ap_tweet_list[1][2], ap_tweet_list[1][3], ap_tweet_list[1][4], ap_tweet_list[1][5], ap_tweet_list[1][6], ap_tweet_list[1][7], ap_tweet_list[1][8], ap_tweet_list[1][9], ap_tweet_list[1][10], ap_tweet_list[1][11], ap_tweet_list[1][12], ap_tweet_list[1][13], ap_tweet_list[1][14], ap_tweet_list[1][15], ap_tweet_list[1][16], ap_tweet_list[1][17], ap_tweet_list[1][18], ap_tweet_list[1][19]
        ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8, ch9, ch10, ch11, ch12, ch13, ch14, ch15, ch16, ch17, ch18, ch19, ch20 = tweet_full(ap_tweet_list[0][0]), tweet_full(ap_tweet_list[0][1]), tweet_full(ap_tweet_list[0][2]), tweet_full(ap_tweet_list[0][3]), tweet_full(ap_tweet_list[0][4]), tweet_full(ap_tweet_list[0][5]), tweet_full(ap_tweet_list[0][6]), tweet_full(ap_tweet_list[0][7]), tweet_full(ap_tweet_list[0][8]), tweet_full(ap_tweet_list[0][9]), tweet_full(ap_tweet_list[0][10]), tweet_full(ap_tweet_list[0][11]), tweet_full(ap_tweet_list[0][12]), tweet_full(ap_tweet_list[0][13]), tweet_full(ap_tweet_list[0][14]), tweet_full(ap_tweet_list[0][15]), tweet_full(ap_tweet_list[0][16]), tweet_full(ap_tweet_list[0][17]), tweet_full(ap_tweet_list[0][18]), tweet_full(ap_tweet_list[0][19])

        # ap1, ap2, ap3, ap4, ap5, ap6, ap7, ap8, ap9, ap10, ap11, ap12, ap13, ap14, ap15, ap16, ap17, ap18, ap19, ap20 = ap_tweet_list[1][0], ap_tweet_list[1][1], ap_tweet_list[1][2], ap_tweet_list[1][3], ap_tweet_list[1][4], ap_tweet_list[1][5], ap_tweet_list[1][6], ap_tweet_list[1][7], ap_tweet_list[1][8], ap_tweet_list[1][9], ap_tweet_list[1][10], ap_tweet_list[1][11], ap_tweet_list[1][12], ap_tweet_list[1][13], ap_tweet_list[1][14], ap_tweet_list[1][15], ap_tweet_list[1][16], ap_tweet_list[1][17], ap_tweet_list[1][18], ap_tweet_list[1][19]
        # ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8, ch9, ch10, ch11, ch12, ch13, ch14, ch15, ch16, ch17, ch18, ch19, ch20 = tweet_full(ap_tweet_list[0][0]), tweet_full(ap_tweet_list[0][1]), tweet_full(ap_tweet_list[0][2]), tweet_full(ap_tweet_list[0][3]), tweet_full(ap_tweet_list[0][4]), tweet_full(ap_tweet_list[0][5]), tweet_full(ap_tweet_list[0][6]), tweet_full(ap_tweet_list[0][7]), tweet_full(ap_tweet_list[0][8]), tweet_full(ap_tweet_list[0][9]), tweet_full(ap_tweet_list[0][10]), tweet_full(ap_tweet_list[0][11]), tweet_full(ap_tweet_list[0][12]), tweet_full(ap_tweet_list[0][13]), tweet_full(ap_tweet_list[0][14]), tweet_full(ap_tweet_list[0][15]), tweet_full(ap_tweet_list[0][16]), tweet_full(ap_tweet_list[0][17]), tweet_full(ap_tweet_list[0][18]), tweet_full(ap_tweet_list[0][19])
        return render_template("customtweetchecker.html", **locals())
    else:
        return render_template("customtweetchecker.html", userInput = tweet_scrape.AP_tweet("elonmusk"))

# @app.route('/', methods=['POST'])
# def welcome_post():
#     text = request.form['text']
#     processed_text = text.upper()
#     return processed_text

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
    
    # return render_template("tweetchecker.html", ap1 = ap_tweet_list[1][0], ap2 = ap_tweet_list[1][1], ap3 =ap_tweet_list[1][2], ap4 =ap_tweet_list[1][3], ap5 =ap_tweet_list[1][4], ap6 =ap_tweet_list[1][5], ch1 = tweet_full(ap_tweet_list[0][0]), ch2 = tweet_full(ap_tweet_list[0][1]), ch3 =tweet_full(ap_tweet_list[0][2]), ch4 =tweet_full(ap_tweet_list[0][3]), ch5 =tweet_full(ap_tweet_list[0][4]), ch6 =tweet_full(ap_tweet_list[0][5]) )
    return render_template("tweetchecker.html", **globals() )

@app.route('/tweetinput.html', methods=['GET','POST'])
def tweet_input():

    if request.method == "POST":
    
        user = request.form["nm"]
        return render_template("tweetinput.html", content = user)  
    else:    
	# return render_template("tweetinput.html")
    
        return render_template("tweetinput.html")

if __name__ == '__main__':
    app.run(debug=True)
