#!/usr/bin/env python3  
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Kana Kunikata
# Created Date: 24/03/2022
# version ='1.0'
# ---------------------------------------------------------------------------

""" The implementation of IG Followr main class - IGFollower """


# Import and config ---------------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
from configparser import ConfigParser

config_object = ConfigParser()
config_object.read("config.ini")
general_info = config_object["GENERALINFO"]
ig_arguments = config_object["IGARGUMENTS"]

# IGFollower Class ---------------------------------------------------------------------------


class IGFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get(ig_arguments["ig_login_path"])
        self.login_url = self.driver.current_url
        time.sleep(5)

        username = self.driver.find_element_by_name(ig_arguments["ig_login_username_element_name"])
        password = self.driver.find_element_by_name(ig_arguments["ig_login_password_element_name"])

        username.send_keys(general_info["loginid"])
        password.send_keys(general_info["password"])

        time.sleep(2)
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        self.logined_url = self.driver.current_url

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{general_info['target_account']}")

        time.sleep(5)
        followers = self.driver.find_element_by_xpath(ig_arguments["follower_xpath"])
        followers.click()

        time.sleep(5)
        self.follower_url = self.driver.current_url
        print(self.follower_url)
        modal = self.driver.find_element_by_xpath(ig_arguments["follower_modal_xpath"])
        for i in range(int(ig_arguments["scroll_num"])):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath(ig_arguments["cancel_button_xpath"])
                cancel_button.click()
    def finish(self):
        cancel_button = self.driver.find_element_by_xpath(ig_arguments["cancel_button_xpath"])
        cancel_button.click()
        
