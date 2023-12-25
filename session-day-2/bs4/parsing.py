from bs4 import BeautifulSoup
import requests
import re #this imports support for regular expressions 

url='https://www.manutd.com/'

def tag_selector(tag):
    return tag.name=="div" and tag.has_attr("id") and "homePage" in tag.get("id")

response=requests.get(url)
if response.status_code!=200:
    print("Error in fetching page, please check URL")
    exit()

soup=BeautifulSoup(response.content,'html5lib')

print(soup.find_all(tag_selector))

