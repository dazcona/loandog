#!/usr/bin/python
from random import *
from flask import Flask, render_template, jsonify, request
from flask_bootstrap import Bootstrap
import os
from bson.json_util import dumps
from twitter import get_twitter_data, get_tweets, get_wordcloud
from linkedin import get_linkedin_data
from pdf import get_pdf_data
from transactions import get_transactions_data


# APP
app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")
Bootstrap(app)

# Static path
static_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "static"))


# LANDING
@app.route('/')
def index():
	return render_template('index.html')


# LOAN ESTIMATION
@app.route('/loan')
def main():
    return render_template('loan.html')


# SUCCESS
@app.route('/success')
def success():
	name = request.args.get('name')
	interest = request.args.get('interest')
	money = request.args.get('money')
	duration = request.args.get('duration')
	play = request.args.get('play')
	return render_template('success.html', 
							name=name, 
							interest=interest, 
							money=money, 
							duration=duration,
							play=play)


# TWITTER
@app.route('/twitter')
def twitter():
	username = request.args.get('user').strip()
	if username.startswith('@'): username = username[1:]
	data = get_twitter_data(username)
	return jsonify( data )


# WORDCLOUD
@app.route('/wordcloud')
def wordcloud():
	username = request.args.get('user').strip()
	if username.startswith('@'): username = username[1:]
	words = get_tweets(username)
	path = get_wordcloud(username, words)
	image = dict(desc='WordCloud', path=path)
	return render_template('figure.html', image=image)


# LINKEDIN
@app.route('/linkedin')
def linkedin():
    uri = request.args.get('uri')
    data = get_linkedin_data(uri)
    return jsonify( data )


# TRANSACTIONS
@app.route('/transactions')
def transactions():
	transactions = get_transactions_data()
	data = [ list(t / 25000) for t in transactions ]
	return render_template('transactions.html', data=data)


# PDF
@app.route('/transcripts')
def pdf():
    data = get_pdf_data(filename)
    return jsonify( data )


# INTEREST RATE'S BALL
@app.route('/ball')
def ball():
    return render_template('ball.html')


# PIE CHART
@app.route('/pie')
def pie():
	data = [2, 4, 1, 6, 2, 4, 5]
	return render_template('pie.html', data=data)


# CATEGORIES CHART
@app.route('/categories')
def categories():
	data = [ 
		[ randint(1,1000) ] * 31, 
		[ randint(1,1000) ] * 31, 
		[ randint(1,1000) ] * 31, 
		[ randint(1,1000) ] * 31, 
		[ randint(1,1000) ] * 31,
	]
	return render_template('categories.html', data=data)


# WORDS CHART
@app.route('/words')
def words():
	return render_template('words.html')


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
