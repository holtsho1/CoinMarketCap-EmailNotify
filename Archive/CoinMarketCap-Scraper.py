#https://stackoverflow.com/questions/66508843/how-can-to-keep-a-python-script-running-on-the-web-server-hosting

# Import requests (to download the page)
import requests

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# Import Time (to add a delay between the times the scape runs)
import time

# Import smtplib (to allow us to email)
import smtplib


# This is a pretty simple script. The script downloads the homepage of VentureBeat, and if it finds some text, emails me.
# If it does not find some text, it waits 60 seconds and downloads the homepage again.

# set the url as you please,
url = "https://coinmarketcap.com/new/"
# set the headers like we are a browser,
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ Safari/537.36'}
# download the homepage
response = requests.get(url, headers=headers)
# parse the downloaded homepage and grab all text, then,
soup = BeautifulSoup(response.text, "lxml")
parsed_data=open('Parsed-Data.txt','w')

parsed_data.write(str(soup))
parsed_data.close()
# to create the initial hash
print("running")
time.sleep(1)
while True:
	parsed_data=open('Parsed-Data.txt','r')
	content=parsed_data.read()
	location=content.index('"recentlyAddedList"')
	parsed_data.seek(location)
	location=content.index('"name"')
	parsed_data.seek(location+7)
	if content[index]=='"':
                
		# perform the get request and store it in a var
		response = requests.get(url, headers=headers)
		soup = str(BeautifulSoup(response.text, "lxml"))
		# create a hash
		#currentHash = hashlib.sha224(response).hexdigest()
		
		# wait for 30 seconds
		time.sleep(60)
		
		# perform the get request
		response = requests.get(url, headers=headers)
		
		# create a new hash
		#newHash = hashlib.sha224(response).hexdigest()

		# check if new hash is same as the previous hash

		
		# notify
		print("New coin added")
		#write email notification
		SendGmailFunc()
		# again read the website
		response = requests.get(url, headers=headers)

		# create a hash
		#currentHash = hashlib.sha224(response).hexdigest()

		# wait for 30 seconds
		time.sleep(60)
		#continue
			
	# To handle exceptions
	#except Exception as e:
		#print("error")
