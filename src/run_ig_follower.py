#!/usr/bin/env python3  
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Kana Kunikata
# Created Date: 24/03/2022
# version ='1.0'
# ---------------------------------------------------------------------------

""" The runner script that invokes IGFollowr class for execution of IG-follower app """


from ig_follower_main import IGFollower
chrome_path=r"C:\Users\pauyan01\Desktop\Python pick 2-3 projects\1_IG follower\ForDeveloper2\ig_follower_refactor\chromedriver_win32_ver99\chromedriver.exe"


bot = IGFollower(chrome_path)
bot.login()
bot.find_followers()
bot.follow()
bot.finish()