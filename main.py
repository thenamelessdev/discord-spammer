import requests
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_dir, "token.txt")

with open(file_path, "r") as file:
    token = file.read()



def send_message():
    channelid = input("Write the target channel ID here: ")
    message = input("What should be the message? Type it here: ")
    headers = {
        "Authorization": token
    }
    body = {
        "content": message
    }
    request = requests.post(f"https://discord.com/api/v10/channels/{channelid}/messages", headers=headers, json=body)
    print(request)

send_message()