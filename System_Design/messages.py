from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

# login to Heny
driver.get("https://heny.com")
time.sleep(5)

# Enter your login details here
username = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button/span[2]')
username.click()
time.sleep(2)

username_fb = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]')
username_fb.click()
time.sleep(2)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

fb_email = driver.find_element_by_id("email")
fb_email.send_keys("Enter your email id here")
time.sleep(2)

fb_pass = driver.find_element_by_id("pass")
fb_pass.send_keys("Enter your password here")
time.sleep(2)

fb_login = driver.find_element_by_id("loginbutton")
fb_login.click()
time.sleep(2)

driver.switch_to.window(base_window)

# message other users
while True:
    try:
        message_button = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        message_button.click()
        time.sleep(2)

        message_field = driver.find_element_by_xpath('//*[@id="chat-text-area"]')
        message_field.send_keys("Enter your message here")
        time.sleep(2)

        send_button = driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/div[3]/form/button')
        send_button.click()
        time.sleep(2)

    except:
        print("No more users to message")
        break