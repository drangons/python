import sys
import urllib
url= r'http://beta.appinventor.mit.edu/learn/tutorials/hellopurr/HelloPurrAssets/meow.mp3'

print url
urllib.urlretrieve(url,'meow.mp3')
