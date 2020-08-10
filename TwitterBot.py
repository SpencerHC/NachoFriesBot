# Written by Spencer Conley
# Tweets about Nacho Fries
import time
import urllib3
from bs4 import BeautifulSoup
import tweepy


def main():
    twitter = tweepyAuth()

    while (True):
        areFriesBack = isIdThere('https://www.tacobell.com/search?text=Nacho+Fries&storeNumber=', "product-name", "Nacho Fries")
        if areFriesBack == False:
            twitter.update_status('Still waiting..')
        else:
            twitter.update_status('The Fries are here!')
        time.sleep(86400) #runs daily


def tweepyAuth():
    # Twitter credentials, returns authenticated API usage
    cKey = 'insert consumer key'
    cSecret = 'inset consumer secret key'
    aKey = 'inset access key'
    aSecret = 'insert access secret key'
    auth = tweepy.OAuthHandler(cKey, cSecret)
    auth.set_access_token(aKey, aSecret)
    return tweepy.API(auth)


def isIdThere(url, className, id):
    # Takes strings, returns boolean
    # URL you want to search for, name of the class and then id you are searching for.
    # Made semi dynamically for possible future use in webscraping bots
    http = urllib3.PoolManager()
    actualSite = http.request('GET', url)
    soup = BeautifulSoup(actualSite.data)
    SearchProd = soup.find('div', class_=className)
    foundId = SearchProd.a.contents
    print(foundId[0])
    if foundId[0] == id:
        return True
    else:
        return False


main()
