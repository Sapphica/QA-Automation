# !/usr/bin/env python3  Line 1
# -*- coding: Windows-1252 -*- Line 2
from selenium import webdriver  # import selenium to the file
from selenium.webdriver.chrome.service import Service
from time import sleep
import datetime
from selenium.webdriver.common.by import By
import aos_locators
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Headless
# from selenium.webdriver.chrome.options import Options
# options = Options()
# options.add_argument("--headless")
# options.add_argument("window-size=1400,1500")
# options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")
# options.add_argument("start-maximized")
# options.add_argument("enable-automation")
# options.add_argument("--disable-infobars")
# options.add_argument("--disable-dev-shm-usage")
# driver = webdriver.Chrome(options=options)

# none headless
s = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.maximize_window()

st = 0.25  # sleep time
driver.implicitly_wait(20)
driver.get(aos_locators.aos_url)

infinity = ''' /\.../\          
              (  •.•  )           
               ..=*=..            
          **~~( \.||./ )  ©Shawna '''

def setUp():
    if driver.current_url == aos_locators.aos_url and driver.title == aos_locators.aos_home_page_title:
        print('Advantage has Launched Successfully')
        print(f'Homepage URL:{driver.current_url}\nHome Page Tittle = {driver.title}')
        sleep(st)
    else:
        print(f'Advantage did not launch')
        print(f'Current:{driver.current_url}\nHome Page Tittle {driver.title}')

def tearDown():
    if driver is not None:
        print('--------------------~*~--------------------\nClosing Browser\n--------------------~*~--------------------')
        print(f'The test Completed at: {datetime.datetime.now()}')
        sleep(st)
        driver.close()
        driver.quit()

def adduser():
    sleep(1)
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
    sleep(st)
    for r in range(len(aos_locators.list_reg)):
        reg, vars, = aos_locators.list_reg[r], aos_locators.list_vars[r]
        sleep(st)
        driver.find_element(By.XPATH, f'//input[contains(@name, "{reg}")]').send_keys(vars)
    sleep(st)
    driver.find_element(By.XPATH, '//option[contains(@label, "Canada")]').click()
    driver.find_element(By.XPATH, '//input[contains(@name, "i_agree")]').click()
    sleep(st)
    driver.find_element(By.ID, 'register_btnundefined').click()
    sleep(st)
    assert driver.find_element(By.XPATH, f'//*[contains(.,"{aos_locators.new_username}")]').is_displayed()
    print(f'--------------------~*~--------------------\nUser name {aos_locators.new_username} has been\
 created. Assert is Successful')
    logger('Created')
    sleep(st)

def logout():
    print('--------------------~*~--------------------')
    driver.find_element(By.ID, 'hrefUserIcon').click()
    java_script = driver.find_element(By.XPATH, '//label[contains(.,"Sign out")]')
    driver.execute_script("arguments[0].click();", java_script)
    print(f'User {aos_locators.new_username} has logged out')

def login():
    sleep(1)
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(st)
    driver.find_element(By.XPATH, '//input[contains(@name, "username")]').send_keys(aos_locators.new_username)
    sleep(st)
    driver.find_element(By.XPATH, '//input[contains(@name, "password")]').send_keys(aos_locators.new_password)
    sleep(st)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    print(f'--------------------~*~--------------------\n{aos_locators.new_username} with pass {aos_locators.new_password} logged in')
    assert driver.find_element(By.XPATH, f'//*[contains(.,"{aos_locators.new_username}")]').is_displayed()
    print(f'User name {aos_locators.new_username} Assert is Successful')
    sleep(st)

def topmenu():
    global ass, soc
    print('--------------------~*~--------------------')
    for r in range(len(aos_locators.list_ass)):
        ass = aos_locators.list_ass[r]
        sleep(st)
    assert driver.find_element(By.XPATH, f'//*[contains(.,"{ass}")]').is_displayed()
    print(f'Assertion on {aos_locators.list_ass}')
    driver.find_element(By.LINK_TEXT, 'SPECIAL OFFER').click()
    print('Special Offer has been clicked')
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'POPULAR ITEMS').click()
    print('Popular Items has been clicked')
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'CONTACT US').click()
    print('Contact US has been clicked')
    sleep(1)

def contact_us():
    print('--------------------~*~--------------------')
    assert driver.find_element(By.LINK_TEXT, 'CONTACT US').is_displayed()
    print('Assertion on Contact Us successful')
    driver.find_element(By.XPATH, '//option[contains(@label, "Laptops")]').click()
    driver.find_element(By.XPATH, '//option[contains(@label, "HP Pavilion 15z Laptop")]').click()
    driver.find_element(By.NAME, 'emailContactUs').send_keys(aos_locators.email)
    driver.find_element(By.NAME, 'subjectTextareaContactUs').send_keys(aos_locators.kitty)
    sleep(1)
    driver.find_element(By.ID, 'send_btnundefined').click()
    print('Contact Form Sent')
    assert driver.find_element(By.LINK_TEXT, 'CONTINUE SHOPPING').is_displayed()
    for r in range(len(aos_locators.list_social)):
        soc = aos_locators.list_social[r]
        sleep(st)
    assert driver.find_element(By.NAME, f'{soc}').is_displayed()
    print(f'Assertion on {aos_locators.list_social}')
    driver.find_element(By.LINK_TEXT, 'CONTINUE SHOPPING').click()

def shoppingcart():
    global order
    print('--------------------~*~--------------------')
    print(f'Adding product #{aos_locators.rand} to shopping cart')
    driver.get(f'{aos_locators.cart}')
    item = driver.find_element(By.XPATH, '//h1[contains(@class,"roboto-regular screen768 ng-binding")]')
    print(f'Item added {item.text}')
    # if driver.find_element(By.CLASS_NAME, 'OutOfStock') == True:
    #     shoppingcart()
    # else:
    driver.find_element(By.NAME, 'save_to_cart').click()
    sleep(st)
    driver.find_element(By.NAME, 'check_out_btn').click()
    sleep(st)
    driver.find_element(By.ID, 'next_btn').click()
    sleep(st)
    driver.find_element(By.NAME, 'safepay_username').send_keys(aos_locators.safe_pay_user)
    sleep(st)
    driver.find_element(By.NAME, 'safepay_password').send_keys(aos_locators.safe_pay_pass)
    sleep(st)
    driver.find_element(By.ID, 'pay_now_btn_SAFEPAY').click()
    sleep(st)
    assert driver.find_element(By.XPATH, '//*[contains(.,"Thank you for buying with Advantage")]').is_displayed()
    print('Order has been Successful')
    for r in range(len(aos_locators.list_order)):
        ord = aos_locators.list_order[r]
        sleep(st)
    assert driver.find_element(By.XPATH, f'//*[contains(.,"{ord}")]').is_displayed()
    print(f'Assert on {aos_locators.list_order}')
    sleep(st)
    track = driver.find_element(By.ID, 'trackingNumberLabel')
    order = driver.find_element(By.ID, 'orderNumberLabel')
    total = driver.find_element(By.XPATH, "//label[contains(.,'TOTAL')]/a[@class='floater ng-binding']")
    date = driver.find_element(By.XPATH, "//label[contains(.,'Date ordered')]/a[@class='floater ng-binding']")
    order, track, date, total = order.text, track.text, date.text, total.text
    print(f'Tracking number found: {track}\nOrder number found: {order}\nOrder date found: {date}\nTotal for order found = {total}')
    sleep(st)

def delete_user():
    print('--------------------~*~--------------------')
    driver.find_element(By.ID, 'hrefUserIcon').click()
    java_script = driver.find_element(By.XPATH, '//label[contains(.,"My account")]')
    driver.execute_script("arguments[0].click();", java_script)
    sleep(1)
    assert driver.find_element(By.XPATH, f'//*[contains(.,"MY ACCOUNT")]').is_displayed()
    print('Assertion done on My Account')
    driver.find_element(By.CLASS_NAME, 'deleteBtnText').click()
    sleep(st)
    assert driver.find_element(By.CLASS_NAME, 'deleteBtnContainer').is_displayed()
    driver.find_element(By.CLASS_NAME, 'deleteBtnContainer').click()
    print(f'Account {aos_locators.new_username} has been Deleted')
    logger('Deleted')

def orders():
    print('--------------------~*~--------------------')
    print('Checking order page')
    driver.find_element(By.ID, 'hrefUserIcon').click()
    java_script = driver.find_element(By.XPATH, '//label[contains(.,"My orders")]')
    driver.execute_script("arguments[0].click();", java_script)
    assert driver.find_element(By.XPATH, f'//*[contains(.,"MY ORDERS")]').is_displayed()
    print('Assertion done on My Orders')
    assert driver.find_element(By.XPATH, f'//*[contains(.,"{order}")]').is_displayed()
    print(f'Order has been found: {order}')
    sleep(st)

def logger(action):
    old_instance = sys.stdout
    log_file = open('message.log', 'a')  # open log file and append a record
    sys.stdout = log_file
    print(f'{aos_locators.new_username}\t'
          f'{aos_locators.new_password}\t'
          f'{datetime.datetime.now()}\t'
          f'{action}')
    sys.stdout = old_instance
    log_file.close()

# # # # #
# setUp()
# adduser()
# # #
# # # # # # login()
# shoppingcart()
# orders()
# # # # delete_user()
# # # # # # # # topmenu()
# # #
# # # orders()
# # # delete_user()