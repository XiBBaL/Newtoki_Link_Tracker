import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import os

location = os.getcwd()
num = 216

def OpenGDPI():
    os.system(str(location) + "/GDPI64/goodbyedpi.exe") #launch GoodbyeDPI for bypass HTTPS censorship (Required sometimes)

def OpenTab(url_num):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    chrome_options.add_argument('incognito')
    chrome_options.add_argument('--start-maximized')

    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)


    # bypassing Anti-Crawling-bot and counterfeit profile
    chrome_options.add_argument("disable-gpu")   # disable GPU acceleration
    chrome_options.add_argument("lang=ko_KR")    # Adapt Fake Plug-in
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 위조
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation']) # Delete "Automation Software" popups
 
    tabs = driver.window_handles
 
    driver.switch_to.window(tabs[0])
    driver.get(f'https://newtoki{url_num}.com/webtoon?toon=성인웹툰')
    
header_example = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'
}

base_url = "https://newtoki216.com/"

current_respond = str(requests.get(base_url, headers=header_example))
print(f"Respond Code is {current_respond} now")

def check_and_open():
    global num
    global current_respond
    if current_respond == "<Response [200]>":
        OpenTab(num) #basically 216
        print("Done! Enjoy!")
        
    else:
        if num > 999:
            print("OOPs.. I cannot track URL. Try Manually.")
            
        else:
            num += 1
            fixed_url = f"https://newtoki{num}.com/"
            current_respond = str(requests.get(fixed_url))
            print(f"Trying {num}")
            check_and_open()
            
        
print("Welcome to Newtoki Link Tracker!\n\nSometimes, in the case site is blocked by government censorship, program doesnt work. In this case, launch GoodbyeDPI alone first and launch chrome tab later.\n")
work = int(input("Type 0 for launch all\nType 1 for launch GoodbyeDPI\nType 2 for open NEWTOKI chrome tab\nType 3 for see Program Info\n"))

if work == 0:
    check_and_open()
    OpenGDPI()
elif work == 1:
    OpenGDPI()
elif work == 2:
    check_and_open()
elif work == 3:
    print("Copyright 2023. XiBBaL all rights reserved.\nVersion : 1.0.0\nIf you want to know more about this program, visit \'https://github.com/XiBBaL/newtoki_link_tracker\'\nThanks!")
    sleep(10)
else:
    print("Type Valid Number\n")
    sleep(3)
