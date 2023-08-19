# Texas A&M University Class Registration Notifier

This Python script continuously checks seat availability for a class at Texas A&M University. When a seat becomes available, the script sends a notification to a specified Discord channel using a webhook. 

## Prerequisites

1. Python 3.x
2. Google Chrome browser (as the script uses the Chrome webdriver)
3. Libraries: `selenium` and `requests`
   
   Install them using:
   ```bash
   pip install selenium requests
   ```

4. ChromeDriver: Ensure you have [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) downloaded and added to your system's PATH, or the same location as your script.

## Setup

1. Update the `DISCORD_WEBHOOK_URL` variable in the script with your Discord webhook URL.
2. If the URL of the registration page changes in the future, update the `REGISTRATION_URL` variable.

## How to Use

1. Run the script:
   ```bash
   python main.py
   ```

2. A Chrome browser window will open, navigating to the registration page.
3. Manually log in to the registration portal using your credentials.
4. After choosing your registration term, find the course you want to monitor under "Courses" and click on the sections button next to it to bring up all of the available sections.
4. After navigating to the sections page of the class, go back to the terminal and press `Enter` to continue.
5. The script will check for seat availability every 60 seconds. If a seat is available, you'll get a notification on Discord

## Notes

- The script uses a specific CSS selector (`span.css-1np60a3-highlightCss`) to detect seat availability. If the website's structure changes in the future, you may need to update this selector.
