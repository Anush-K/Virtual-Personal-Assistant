import requests
import pywhatkit as kit

def my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

def youtube(video):
    kit.playonyt(video)

def google_search(query):
    kit.search(query)

def WA_msg(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)

def tell_a_joke():
    headers = {
        'Accept': 'application/json'
    }
    result = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return result["joke"]
