import time

import pyperclip
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def open_url(page_url, page_title):
    driver.maximize_window()
    driver.get(page_url)
    wait.until(EC.title_is(page_title))
    return driver


url = 'http://jsonviewer.stack.hu/'
title = 'Online JSON Viewer'
failed_screenshot_path = '..\\FailedScreenshots\\'

try:
    driver = webdriver.Chrome(executable_path='..\\SeleniumDrivers\\chromedriver.exe')
    wait = WebDriverWait(driver, 10)
    open_url(url, title)

    # copy + paste from json file into the text editor element
    edit_text_element = driver.find_element_by_id("edit")
    edit_text_element.clear()
    try:
        filename = open('einat_world_bank.json', encoding="utf8")
        file_content = filename.read()
        filename.close()
        pyperclip.copy(file_content)
        edit_text_element.send_keys(Keys.CONTROL, 'v')
    except FileNotFoundError:
        print("File was not found!")

    # click on the format button
    driver.find_element_by_id('ext-gen60').click()
    time.sleep(2)

    # validate that the web browser contains the value ‘090224b0817be218_1_0’
    text_element_content = edit_text_element.get_attribute("value")
    if text_element_content.find('090224b0817be218_1_0') != -1:
        print("Web browser contains the value {0}".format('090224b0817be218_1_0'))
        path = driver.save_screenshot(failed_screenshot_path+'text_found.png')
        print("'Invalid_JSON_variable' error appeared. Screenshot taken and saved to {0}".format(failed_screenshot_path))

    # click on the Viewer tab
    driver.find_element_by_xpath('//*[@id="ext-comp-1004__viewerPanel"]/a[2]/em/span/span').click()

    # checks if the 'Invalid JSON variable' error message is displayed - if it does a screenshot is taken
    try:
        if driver.find_element_by_id("ext-gen110").is_displayed():
            time.sleep(2)
        path = driver.save_screenshot(failed_screenshot_path+'error_message.png')
        print("'Invalid_JSON_variable' error appeared. Screenshot taken and saved to {0}".format(failed_screenshot_path))
    except NoSuchElementException as error:
        print("Element not found\n", error)

finally:
    driver.quit()
