from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys
from time import sleep

URL = "https://tinder.com"
MAIL_ID = "YOUR EMAIL ID"
PASSWORD = "FACEBOOK PASSWORD"

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
browser.maximize_window()
browser.get(url=URL)

sleep(2)
cookies = browser.find_element(By.XPATH,"//*[text()='I decline']")
cookies.click()

sleep(2)
log_in = browser.find_element(By.XPATH,"//*[text()='Log in']")
log_in.click()

sleep(2)
more_options = browser.find_element(By.XPATH,"//*[text()='More Options']")
more_options.click()

sleep(2)
facebook = browser.find_element(By.XPATH,"//*[text()='Log in with Facebook']")
facebook.click()
sleep(7)
browser.switch_to.window(browser.window_handles[1])

sleep(2)
email = browser.find_element(By.XPATH,"//*[@id='email']")
email.send_keys(MAIL_ID)

sleep(2)
password = browser.find_element(By.XPATH,"//*[@id='pass']")
password.send_keys(PASSWORD+Keys.ENTER)
sleep(7)
browser.switch_to.window(browser.window_handles[0])

sleep(5)

location = browser.find_element(By.XPATH,"//*[text()='Allow']")
location.click()

sleep(3)
denied = browser.find_element(By.XPATH,"//*[text()='Not interested']")
denied.click()

sleep(5)
dislike = browser.find_element(By.XPATH,"//*[text()='Maybe Later']")
dislike.click()

sleep(5)
like = browser.find_element(By.XPATH,'//*[@id="Tinder"]/body')
like.send_keys(Keys.ARROW_RIGHT)
sleep(4)
for i in range(20):
    try:
        like.send_keys(Keys.ARROW_RIGHT)
    except:
        browser.quit()
    sleep(3)
browser.quit()

sleep(5)







