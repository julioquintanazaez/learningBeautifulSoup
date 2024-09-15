#from urllib.request import urlopen 
import requests
from bs4 import BeautifulSoup 
import os
import urllib3
import filetype
import urllib.request


headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
# Here the user agent is for Edge browser on windows 10. You can find your browser user agent from the above given link.

def create_dir(dir_name):
	# Parent Directory path
	parent_dir = os.path.dirname(os.path.realpath(__file__))
	# Path
	path = os.path.join(parent_dir, dir_name)
	try:
		os.mkdir(path)    	
	except OSError as e:
		print('The file directory already exist: ', e)
	return path

def download_image(url, save_path):
	response = requests.get(url, headers=headers)
	if response.status_code != 200:
		return "Cant download the file"
	with open(save_path, 'wb') as f:
		f.write(response.content)

#htmldata = urlopen('https://www.geeksforgeeks.org/') 
url = 'https://www.geeksforgeeks.org'  #https://www.passiton.com/inspirational-quotes
data = requests.get(url, headers=headers).text  
soup = BeautifulSoup(data, 'html.parser') 
#Read all the images
images = soup.find_all('img') 
for item in images: 
	print(item['src']) 

#Save all images
dir_name = "download"
root_dir = create_dir(dir_name)

for img in images:
	try: 
		fi = img['src'].split("/")
		path = root_dir + "/" + fi[len(fi)-1]
		download_image(img['src'], path)
	except IOError as e:
		print(e)
		 
