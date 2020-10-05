#Lab 4
import http.client
import urllib
import time
key = "54CDA6FJF4RCJ92C"

#info to be uploaded
Cmail = "Nathanmezzomo@cmail.carleton.ca"
Group = "L2-M-13"
identifier = "a"

#Identifying the parameters and key
params = urllib.parse.urlencode({'field1': Cmail, 'field2': Group, 'field3': identifier, 'key':key }) 
headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
conn = http.client.HTTPConnection("api.thingspeak.com:80")
#uploading data
conn.request("POST", "/update", params, headers)
