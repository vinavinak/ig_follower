from configparser import ConfigParser

#Get the configparser object
config_object = ConfigParser()

#we need 2 sections in the config file, let's call them GENERALINFO and IGARGUMENTS
config_object["GENERALINFO"] = {
    "loginid": "",
    "password": "",
    "target_account":"",
    "chrome_driver_path":r''
}


config_object["IGARGUMENTS"] = {
    "follower_xpath": '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a',
    "ig_login_path": "https://www.instagram.com/accounts/login/",
    "follower_modal_xpath":'/html/body/div[6]/div/div/div',
    "cancel_button_xpath":'/html/body/div[6]/div/div/div/div[1]/div/div[2]/button',
    "ig_login_username_element_name":"username",
    "ig_login_password_element_name":"password",
    "scroll_num":'2'
}


#Write the above sections to config.ini file
with open('config.ini', 'w', encoding="utf-8") as conf:
    config_object.write(conf)