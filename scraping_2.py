#https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/
#https://stackoverflow.com/questions/2935658/beautifulsoup-get-the-contents-of-a-specific-table
#https://medium.com/geekculture/web-scraping-tables-in-python-using-beautiful-soup-8bbc31c5803e
#https://stackoverflow.com/questions/2136267/beautiful-soup-and-extracting-a-div-and-its-contents-by-id
#https://stackoverflow.com/questions/71475190/finding-all-div-elements-with-varying-id-value-with-beautifulsoup
#pip install requests
#pip install html5lib
#pip install bs4

import requests	
from bs4 import BeautifulSoup 
import csv

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
url = 'https://www.passiton.com/inspirational-quotes'
data = requests.get(url, headers=headers).text  
soup = BeautifulSoup(data, 'lxml') 
quotes=[]  # a list to store quotes 
table = soup.find_all('div', class_='col-6 col-lg-4 text-center margin-30px-bottom sm-margin-30px-top')
for row in table:
	quote = {}
	quote['img'] = row.img['src']
	quote['lines'] = row.img['alt'].split("#")[0]
	quotes.append(quote)
	
filename = 'inspirational_quotes.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['img','lines'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)
	
print(len(quotes))
