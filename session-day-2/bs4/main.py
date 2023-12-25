from bs4 import BeautifulSoup
import requests

url='https://www.passiton.com/inspirational-quotes'
r=requests.get(url)
soup=BeautifulSoup(r.content,'html5lib')
print(soup.prettify())

#soup object can be very useful in parsing various sections of html page
print(soup.title)

print(soup.title.string)

no_oflinks=len(soup.find_all('a'))
print(f"there are {no_oflinks}links in this page")
#find gives you the first matching element. if you dont just want the first matching element use findall 

print(soup.get_text())

#parsing through html tags
first_link=soup.a
print(first_link)
print(first_link.text)#gives text of first anchor tag
print(first_link.href)#gives the reference link of first anchor tag

#finding elements from their id/class names
element=soup.find(id="pagespace")
print(element)

element2=soup.find(class_="athing")
print(element2)

# now we have gone through the basics. Lets try to find the top 3 most occuring links on this page. for this we will be importing the counter function from collections libraries  of python
from collections import Counter
al_href=[a.get('href') for a in soup.find_all('a')] #this is a way of writing multiple lines of code in a single line.
top_3links=Counter(al_href).most_common(3)               #most_common(n) gives the n most common elements in the given parameter
print(top_3links)
