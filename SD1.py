# this script scrapes the article links from the front
# page of Gizmodo.co.uk
import requests
import bs4
import webbrowser

# the requests.get status will pull the HTML from the page
# raise for status will check if there are any errors
target_url = requests.get('http://www.gizmodo.co.uk/')
target_url.raise_for_status()

# sets the content from the page to a variant and parses it
# with beautiful soup
html = target_url.content
soup = bs4.BeautifulSoup(html,'lxml')

# creates an empty list and adds in each link
link_list = []
for link in soup.find_all('a'):
 link_list.append(link.get('data-disqus-url'))

# removes the 'None' links
# there are multiple links on the page which aren't 
# 'main' links and we don't want these
link_list = filter(None,link_list)

# next step - launch if not quit
OpenAgain = 'Y'
link_coupon = 0
link_value = link_list[link_coupon]

while OpenAgain == 'Y':
	webbrowser.open(link_value)
	link_coupon = link_coupon + 1
	OpenAgain = raw_input('Continue? Press Y for More!')

print 'Had enough then!'