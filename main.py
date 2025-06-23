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

def createguild():
    headers = {
        "Authorization": token
    }
    body = {
        "name": name
    }
    creareserver = requests.post("https://discord.com/api/guilds", headers=headers, json=body)
    print(creareserver)


def createchannel():
    headers = {
        "Authorization": token
    }
    body = {
        "name": name,
        "type": "GUILD_TEXT"
    }
    request = requests.post(f"https://discord.com/api/v10/guilds/{serverid}/channels", headers=headers, json=body)
    print(request)

def sendwebhookmsg():
    body = {
        "content": msg
    }
    request = requests.post(url, json=body)
    print(request)

def deletewebhook():
    request = requests.delete(url)
    print(request)

def createwebhook():
    body = {
        "name": name
    }
    headers = {
        "Authorization": token
    }
    request = requests.post(f"https://discord.com/api/v10/channels/{channelid}/webhooks", json=body, headers=headers)

spammer = input("What spammer would you like to use? 1: Message spammer 2: Join-then-leave spammer 3: Make servers 4: Channel maker 5: Webhook spammer (not uses your user token). Answer here: ")

if spammer == "1": 
    channelid = input("Write the target channel ID here: ")
    message = input("What should be the message? Type it here: ")
    while True:
        send_message()
elif spammer == "2":
    invite = input("Put the server invite code here: ")
    while True:
        jointhenleave()
elif spammer == "3":
    name = input("What should be the server name: ")
    while True:
        createguild()
        time.sleep(1)
elif spammer == "4":
    print("Make sure that you have the manage channels premission.")
    serverid = input("What is the server ID of the taeget server: ")
    name = input("What should be the channel name: ")
    while True:
        createchannel()
elif spammer == "5":
    url = input("Paste your webhook link here: ")
    msg = input("Type the message here: ")
    while True:
        sendwebhookmsg()
        time.sleep(0.5)
elif spammer == "6":
    name = input("Type the webhook name here: ")
    channelid = input("Type the channel ID here: ")
    while True:
        createwebhook()
        time.sleep(0.1)

else:
    print(f"{spammer} is not in the list.")