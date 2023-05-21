from sp_engine import greet_user, take_user_input, speak
from online_ops import my_ip, youtube, google_search,WA_msg,tell_a_joke
from offline_ops import calculator, camera, cmd, notepad,say_time

if __name__ == '__main__':
    greet_user()
while True:
    query = str(take_user_input()).lower()

    if 'open notepad' in query:
        notepad()

    elif 'open command prompt' in query or 'open cmd' in query:
        cmd()

    elif 'open camera' in query:
        camera()

    elif 'open calculator' in query:
        calculator()

    elif 'ip address' in query:
        ip_address = my_ip()
        speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen .')
        print(f'Your IP Address is {ip_address}')
    
    elif 'youtube' in query:
        speak('What do you want to play on Youtube?')
        video = take_user_input().lower()
        youtube(video)

    elif ('search on google' in query or 'search' in query or 'google' in query):
        speak('What do you want to search on Google?')
        query = take_user_input().lower()
        google_search(query)

    elif "whatsapp" in query:
        speak('To what number should I send the message ? Please enter in the console: ')
        number = input("Enter the whatsapp number: ")
        speak("What is the message?")
        message = take_user_input().lower()
        WA_msg(number, message)
        speak("The message has been sent.")

    elif 'joke' in query:
            speak("Hope you like this one")
            joke = tell_a_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen.")
            print(joke)
    
    elif 'time' in query:
        speak("The time is ")
        speak(say_time())


"""Status = verification()
if(Status):
    greet_user()
while (Status):"""