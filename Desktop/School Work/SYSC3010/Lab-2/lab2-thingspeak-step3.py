#lab2-thingspeak-step3
import requests

URL = 'https://api.thingspeak.com/channels/1154560/feeds.json?api_key=VA52GIBOU4151F7A&results=2'
    
get_data=requests.get(URL).json()
#print(get_data)
channel_id=get_data['channel']['id']
    
field_1=get_data['feeds']
#print(field_1)
    
t=[]
    
for x in field_1:
    t.append(x['field1'])
        
print(t)