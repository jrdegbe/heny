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
# swipe right or left based on the profile compatibility
while True:
    try:
        swipe_right = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        swipe_right.click()
        time.sleep(2)
    except:
        try:
            swipe_left = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
            swipe_left.click()
            time.sleep(2)
        except:
            print("No more profiles to swipe")
            break