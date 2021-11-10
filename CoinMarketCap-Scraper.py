from HTMLParser import *
import time
from SendGmail import *
# to create the initial parse
initial_request=HTMLParser1()

print("running")
time.sleep(30)
while True:

                
        # create a new parse
        request = HTMLParser1()
        print(request)
        # wait for 30 seconds
        time.sleep(30)
                
        # create a new parse
        newRequest = HTMLParser1()
        print(newRequest)
        #check if new hash is same as the previous hash
        if not request==newRequest:
                print("New coin added")  #notify
                #write email notification
                SendGmailFunc()         
        # wait for 30 seconds
        time.sleep(30)
        continue
			
