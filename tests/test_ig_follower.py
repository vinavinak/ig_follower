#!/usr/bin/env python3  
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Kana Kunikata
# Created Date: 24/03/2022
# version ='1.0'
# ---------------------------------------------------------------------------

""" pytest for IGFllower class """

import pytest
import time
from ig_follower_main import IGFollower
chrome_path=r"C:\Users\pauyan01\Desktop\Python pick 2-3 projects\1_IG follower\ForDeveloper2\ig_follower_refactor\chromedriver_win32_ver99\chromedriver.exe"
def test_login():
    bot = IGFollower(chrome_path)
    bot.login()
    assert bot.login_url == 'https://www.instagram.com/accounts/login/'

def test_find_followers():
    bot = IGFollower(chrome_path)
    bot.login()
    time.sleep(2)
    bot.find_followers()
    assert bot.follower_url == 'https://www.instagram.com/buzzfeedtasty/followers/'
    

        




