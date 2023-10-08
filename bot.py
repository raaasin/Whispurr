from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:/Users/dell/AppData/Local/Google/Chrome/User Data")
driver = webdriver.Chrome(options=options)
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 100)

def read_unread_messages():
    while True:
        try:
            # Locate the green indicator for unread messages and click it to open the chat
            unread_indicator = driver.find_element(By.XPATH, '//span[@aria-label="Unread"]')
            unread_indicator.click()

            # Find the latest message within the div
            message_text_element = driver.find_element(By.XPATH, '(//span[@class="_11JPr selectable-text copyable-text"])[last()]')

            # Read and store the latest message
            latest_message = message_text_element.text
            print(latest_message)

            # Process the message using the sendmessage() function
            sendmessage("You said:" + latest_message)

            menu_icon = driver.find_element(By.XPATH, '//span[@data-icon="menu" and @class="kiiy14zj"]')
            menu_icon.click()

        # Locate the "Close chat" button and click it
            close_chat_button = driver.find_element(By.XPATH, '//div[@aria-label="Close chat"]')
            close_chat_button.click()
            
        except:
            # No more unread messages found, wait for a while before checking again
            time.sleep(1)

def sendmessage(message):
    # Locate the message input box and send the message
    message_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')
    message_box.send_keys(message + Keys.ENTER)

# Start reading unread messages continuously
read_unread_messages()