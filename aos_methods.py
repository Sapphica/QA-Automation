# !/usr/bin/env python3  Line 1
# -*- coding: Windows-1252 -*- Line 2

from selenium import webdriver  # import selenium to the file
from selenium.webdriver.chrome.service import Service
from time import sleep
import datetime
from selenium.webdriver.common.by import By
import aos_locators
import sys
# from selenium.webdriver.chrome.options import Options


s = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.maximize_window()
st = 0.25  # sleep time

driver.implicitly_wait(20)
driver.get(aos_locators.aos_url)

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
        print('--------------------~*~--------------------')
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
 created. Assert is Successful.')
    logger('Created')
    sleep(st)

def logout():
    driver.find_element(By.ID, 'hrefUserIcon').click()
    java_script = driver.find_element(By.XPATH, '//label[contains(.,"Sign out")]')
    driver.execute_script("arguments[0].click();", java_script)

def login():
    sleep(1)
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(st)
    driver.find_element(By.XPATH, '//input[contains(@name, "username")]').send_keys(aos_locators.new_username)
    sleep(st)
    driver.find_element(By.XPATH, '//input[contains(@name, "password")]').send_keys(aos_locators.new_password)
    sleep(st)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    print(f'--------------------~*~--------------------\n{aos_locators.new_username} with pass {aos_locators.new_password} logged in.')
    assert driver.find_element(By.XPATH, f'//*[contains(.,"{aos_locators.new_username}")]').is_displayed()
    print(f'User name {aos_locators.new_username} Assert is Successful.')
    sleep(st)

def topmenu():
    print('--------------------~*~--------------------')
    for r in range(len(aos_locators.list_ass)):
        ass = aos_locators.list_ass[r]
        sleep(st)
    assert driver.find_element(By.XPATH, f'//*[contains(.,"{ass}")]').is_displayed()
    print(f'Assertion {aos_locators.list_ass} Detected.')
    driver.find_element(By.LINK_TEXT, 'SPECIAL OFFER').click()
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'POPULAR ITEMS').click()
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'CONTACT US').click()
    sleep(1)
    driver.find_element(By.XPATH, '//option[contains(@label, "Laptops")]').click()
    driver.find_element(By.XPATH, '//option[contains(@label, "HP Pavilion 15z Laptop")]').click()
    driver.find_element(By.NAME, 'emailContactUs').send_keys(aos_locators.email)
    driver.find_element(By.NAME, 'subjectTextareaContactUs').send_keys(aos_locators.kitty)
    sleep(1)
    driver.find_element(By.ID, 'send_btnundefined').click()
    assert driver.find_element(By.LINK_TEXT, 'CONTINUE SHOPPING').is_displayed()
    # for r in range(len(aos_locators.list_social)):
    #     soc = aos_locators.list_social[r]
    #     sleep(st)
    # assert driver.find_element(By.NAME, f'{soc}').is_displayed()
    assert driver.find_element(By.NAME, 'follow_facebook').is_displayed()
    assert driver.find_element(By.NAME, 'follow_twitter').is_displayed()
    assert driver.find_element(By.NAME, 'follow_linkedin').is_displayed()
    print('Assertion done on Social Media links')
    driver.find_element(By.LINK_TEXT, 'CONTINUE SHOPPING').click()

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

#
# setUp()
# topmenu()
# # # adduser()