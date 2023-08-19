import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# URL of the registration page
REGISTRATION_URL = 'https://tamu.collegescheduler.com/'
# Your Discord webhook URL
DISCORD_WEBHOOK_URL = 'WEBHOOK_URL'

def send_discord_notification(message):
    data = {
        "content": message,
        "username": "Registration Bot"
    }
    response = requests.post(DISCORD_WEBHOOK_URL, json=data)
    if response.status_code != 204:
        print(f"Failed to send notification to Discord. Status code: {response.status_code}")

# Start a new instance of the Chrome browser
driver = webdriver.Chrome()

# Navigate to the registration page
driver.get(REGISTRATION_URL)

# Pause the script and wait for you to log in
input("Please log in manually and then press Enter to continue...")

while True:
    sleep(5)
    try:
        # Using the CSS selector to find all elements that indicate seat availability
        availability_elements = driver.find_elements(By.CSS_SELECTOR, 'span.css-1np60a3-highlightCss')
        
        for element in availability_elements:
            print(int(element.text))
            # Check if the number of seats is greater than 0 for any of the elements
            if int(element.text) > 0:
                print("Seat available!")
                
                # You can also add more notifications here, like playing a sound.
                send_discord_notification('Seat Available!')
                
                driver.quit()  # Close the browser
                exit()  # Exit the script

    except Exception as e:
        print(f"Error: {e}")

    print("No seat available yet. Checking again in 60 seconds...")
    sleep(60)
    driver.refresh()