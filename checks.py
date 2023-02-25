from func import *
import secrets
import string

def generate_password(length):
    password = ''.join((secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(length)))
    return password

def check_bot_owner(userid):
    configur = load_json("developers.json")
    if int(userid) in configur['devs']:
        act = True
    else:
        act = False
    return act

def check_premium(guild):
    premium_guilds = load_json("premium.json")
    if premium_guilds[f"{guild}"] == "true":
        premium = True
    else:
        premium = False
    return premium