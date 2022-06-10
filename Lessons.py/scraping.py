from requests import request
import imp
import requests
from bs4 import BeatifulSoup as bs

user_name="JackJr222"
url="https://github.com " + user_name
results=requets.get(url)

soup=bs(results.content, " html parser")
profile_pic = soup.find ('img',{'alt':'Avatar'})['src']
print(profile_pic)
