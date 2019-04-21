#!/usr/bin/python
import random

import sys
import csv
import tweepy
from collections import Counter
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from stopwords import get_stopwords
from random import *
import requests
import config


def get_twitter_data(username):

	return {
		'score': 2,
		'num_words': 10,
		'confidence': 0.75,
	}


def get_tweets(username):

	forbidden_words=["https", "RT", "en", "lo", "de", "the", "a", ""]
	# http://tweepy.readthedocs.org/en/v3.1.0/getting_started.html#api
	auth = tweepy.OAuthHandler(config.BaseConfig.CONSUMER_KEY, config.BaseConfig.CONSUMER_SECRET)
	auth.set_access_token(config.BaseConfig.ACCESS_KEY, config.BaseConfig.ACCESS_SECRET)
	api = tweepy.API(auth)

	# set count to however many tweets you want
	number_of_tweets = 100

	# get tweets
	tweets_for_csv = []
	words = ''
	for tweet in tweepy.Cursor(api.user_timeline, screen_name = username).items(number_of_tweets):
		words += str(tweet.text.encode("utf-8"), 'utf-8')

	stop_words = get_stopwords()
	word_tokens = words.split(" ")
	filtered_sentence = [ w for w in word_tokens if w not in stop_words and "@" not in w and "https" not in w ]
	words = ' '.join(filtered_sentence)

	return words


def get_wordcloud(username, words):

	img_link = 'http://cdn.onlinewebfonts.com/svg/img_74688.png'
	mask = np.array(Image.open(requests.get(img_link, stream=True).raw))

	wordcloud = WordCloud(max_font_size=50, max_words=1000, width=400, height=300,
						background_color="white", mask=mask).generate(words)

	filename = "/web/src/static/wordcloud_{}.png".format(username)
	wordcloud.to_file(filename)

	static_path = filename.split('static/')[1]

	return static_path


def get_message():

	messages = {}

	messages[0] = "You never expect anything from anybody. You're a bit Scottish like that - You don't like to be disappointed and let down. "
	messages[0] += "You are willing to accept the risk, not because it's safe or certain. "
	messages[0] += "Your choices are driven by a desire for discovery. "
	messages[0] += "You are a very impulsive person and you do not stop for a minute to think about how to focus your future."

	messages[1] = "You're not disappointed with bronze. It's always good to come away with a medal. "
	messages[1] += "All your dreams can come true if we have the courage to pursue them. "
	messages[1] += "You consider yourself a persistent person with your goals and even if you do not look for fame, you are interested in doing things well."

	messages[2] = "You are willing to accept a moderate risk, only when it's safe or certain. "
	messages[2] += "The distance between insanity and genius is measured only by success. "
	messages[2] += "Working hard is part of your lifestyle, but you also take time to relax."

	messages[3] = "Opportunities don't happen, you create them. "
	messages[3] += "You dedicate body and soul in everything you decide. There is nothing that could stop you and you always analyze all the exits to choose the one that best suits you. "
	messages[3] += "You live to finish the tasks that you have started, always with the best quality."

	index = random.randint(0, 3)

	return messages[index]
