import bs4
import time as t
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.set_capability('browserVersion', '114.0.5735.110')
chrome_options.set_capability('platformName', 'Windows 10')
driver = webdriver.Remote(
    command_executor='',
    options=chrome_options
)

# from SwipeDown.SwipeDown.UI import UI

def webscrape():

    driver.get('https://www.google.com/?q=')

    title = driver.title
    assert title == 'Web Form'

    driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=By.NAME, value='text-box')
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value='button')
    text_box.send_keys('Selenium')
    submit_button.click()

    message = driver.find_element(by=By.ID, value='message')
    value = message.text
    assert value == 'Recieved!'

    driver.quit()

if __name__ == '__main__':
    webscrape()
