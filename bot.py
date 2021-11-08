import requests
import json
from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = 'Lat nua dien sau'
ACCESS_TOKEN = 'EAAD0oEpZC4WEBABzTi14p3ECbZBP4ZAGPEgCxZBg4cPdZB7gpEsNMZAZBZAyRN5IKqbIPu8sMIuRikSjGhvK2OFl97p5NEQOvGxYepggCAh8gV889HX9bLZCimLxPsQyMSAEdH6T4KOyj9uFKazIKyI8q2OK9IQPrpa8whfeUbDbQD9KrP9JHDjqZAZAoQLjb7kViNH4JtexZCWSZCQZDZD'
@app.route('/', methods=['GET', 'POST'])
def receive_message():
    return ('Hi user')

'''
def get_data():
    response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Hanoi&APPID=738df6f841214ce6867a29562976336d')
    data_str = response.json()
    result = {}
    main = data_str['main']
    temp = main['temp'] 
    temp_max = main['temp_max']
    temp_min = main['temp_min']
    weather = data_str['weather']
    feels = weather[0]['main']
    humidity = main['humidity'] 

    result = {'weather': feels, 'temp': temp, 'temp_min': temp_min, 'temp_max': temp_max, 'huminity': humidity}
    return result
'''

def sendMessage(senderID, message):
    url = 'https://graph.facebook.com/v2.6/me/messages'
    json = {
        'recipient':{
            'ID': senderID
        },
        'message':{
            'text': message
        }
    }
    access_token = 'EAAD0oEpZC4WEBAD9daDmbUNU0PnCUeZAsxrwJh7gxiftvVEZCgwkMSb5psos7p5ZCQbwRZBvpBEGRZCZCncw8GkZCLD4f9sPfZAxPZBZAOd6mbkqhiG1rwWZBEDT2I7pAlD6FSfGHxGRbHYpd0DUKfrpMRW8mjvPBNEgdY4TZBqgmZC2dvPocmJeWZCQdwJ73wPvqhQiGcZBZAZABZCpvjgiQZDZD'
    head = {'Authorization': 'token {}'.format(access_token)}
    requests.post(url=url, json=json, headers=head)

#Code xu ly khi co nguoi nhan tin cho bot
def user_post_message():
    if request.method == 'GET':
        token_sent = request.args.get('hub.verify_token')
        return verify_fb_token(token_sent)
    else:
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    #ID of facebook user
                    recipient_id = message['sender']['id']
                    if message['message'].get('text'):
                        respond_sent_text = get_message()
                        sendMessage(recipient_id, respond_sent_text)
                    if message['message'].get('attachments'):
                        respond_sent_nontext = get_message()
                        sendMessage(recipient_id, respond_sent_text)
    return ('Message Processed')

def verify_fb_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get('hub.challenge')
    return ('Invalid verification token')

#ham tao message gui cho nguoi dung sau khi bot nhan duoc message tu nguoi dung
def get_message():
    #result = get_data()
    message = 'Hello Quang, my name is Linda'
    return message
    
if __name__ == '__main__':
    app.run()
