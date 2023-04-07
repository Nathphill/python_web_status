import sys
import time
import requests
from datetime import datetime


def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    

# Define a list of websites to monitor
websites = ["https://www.google.com", "https://www.facebook.com", "https://www.amazon.com", "https://www.openai.com"]

while True:
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    # Iterate through the websites and check their status codes
    for website in websites:
        try:
            response = requests.get(website)
            if response.status_code == 200:
                typingPrint(f"{current_time}: {website} is up and running.\n")
                print("========================================================================")
            else:
                typingPrint(f"{current_time}: {website} is down. Status code: {response.status_code}\n")
                print("========================================================================")
        except requests.exceptions.RequestException as e:
            typingPrint(f"{current_time}: {website} is down. Error: {e}\n")
            print("========================================================================")
    
    # Wait for 20 seconds before checking the websites again
    time.sleep(20)
