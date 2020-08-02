import h5py
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
import pickle
import re


def tweet_cleaner(s):
    s = re.sub('((https?:\/\/)\S+)', ' ', s)
    s = re.sub('([@]\S+)', ' ', s)
    s = re.sub('[!"$#”“%&\()*+,-./:;<=>?@[\\]^_`{|}~\n]+', '', s)    
    s = re.sub('(RT)', ' ', s)    
    clean_tweet = s
    return clean_tweet

def tweet_tokenizer(text):
    # word_index = pickle.load(open(r"word_index.pickle", "rb" ))

#     file = open(r"D:\Users\Goutham\Documents\BOOTCAMP\Bootcamp Final Project\word_index.pickle",'rb')
    file = open(r"word_index.pickle",'rb')

#     token_file = open(r"D:\Users\Goutham\Documents\BOOTCAMP\Bootcamp Final Project\tokenizer.pickle",'rb')
    token_file = open(r"tokenizer.pickle",'rb')

    word_index = pickle.load(file)

    tokenizer = pickle.load(token_file)
    # with open('tokenizer.pickle', 'rb') as handle:
    #     tokenizer = pickle.load(handle)
    # print(word_index)

    sentence = ["The Oprah Magazine is ending its regular monthly print editions with the December 2020 issue after 20 years of publication. The announcement comes as print advertising shrinks further amid the pandemic."]
    sentences = [
        'I love my dog',
        'I love my cat',
        'You love my dog!',
        'Do you think my dog is amazing?'
    ]

    num_words = 6000
    # tokenizer = Tokenizer(num_words = num_words, oov_token = "<OOV>")

    sequences = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(sequences, maxlen= 28, padding = 'post', truncating= 'post' )
    # tokenizer.fit_on_texts(training_sentences)
    # word_index = tokenizer.word_index
    return padded
    # print(sequences)





