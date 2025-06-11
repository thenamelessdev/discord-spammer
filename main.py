import requests
import os
import time

script_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_dir, "token.txt")

with open(file_path, "r") as file:
    token = file.read()


def send_message():
    headers = {
        "Authorization": token
    }
    body = {
        "content": message
    }
    request = requests.post(f"https://discord.com/api/v10/channels/{channelid}/messages", headers=headers, json=body)
    print(request)

def jointhenleave():
    headers = {
        "Authorization": token
    }

    join = requests.post(f"https://discord.com/api/invites/{invite}", headers=headers)
    print(join)
    time.sleep(0.5)
    leave = requests.delete(f"https://discord.com/api/invites/{invite}", headers=headers)
    print(leave)
    

spammer = input("What spammer would you like to use? 1: Message spammer 2: Join-then-leave spammer: ")

if spammer == "1": 
    channelid = input("Write the target channel ID here: ")
    message = input("What should be the message? Type it here: ")
    while True:
        send_message()
elif spammer == "2":
    invite = input("Put the server invite code here: ")
    while True:
        jointhenleave()