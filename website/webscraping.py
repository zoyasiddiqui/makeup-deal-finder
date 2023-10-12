from bs4 import BeautifulSoup
import requests
import re

def scrape(search):
    
    url = "https://sephora.com/search?keyword="+parse(search)
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0' } 
    page = requests.get(url, headers=headers).text
    doc = BeautifulSoup(page, "html.parser")

    return []

def toItems(items):
    return []

# helper methods
def parse(search):
    word_list = search.split(" ")
    newstr = ""
    for i in range(len(word_list) - 1):
        newstr += word_list[i] + "%20"
    newstr += word_list[-1]
    
    return newstr

# main method
if __name__ == "__main__":
    print(scrape("black honey"))
