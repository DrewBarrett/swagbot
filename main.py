# main.py

import json
from selenium import webdriver
from time import sleep

def main():
    config = json.load(open('config.json'))

    options = webdriver.ChromeOptions()

    #options.add_argument('headless')

    driver = webdriver.Chrome(chrome_options=options)
    #driver = webdriver.Firefox()

    ## wait for user to login
    #while "Login" in driver.title:
    #    sleep(2)
    
    driver.get('http://www.swagbucks.com/earn-money-online')
    driver.delete_all_cookies()

    ## The following are all required to avoid a redirect loop
    driver.add_cookie({'name' : '__urqm', 'value' : config["urqm"], 'path' : '/', 'domain' : '.swagbucks.com'})
    driver.add_cookie({'name' : '__urqc', 'value' : config["urqc"], 'path' : '/', 'domain' : '.swagbucks.com'})
    driver.add_cookie({'name' : 'SBSESSIONID', 'value' : config["SBSESSIONID"], 'path' : '/', 'domain' : 'www.swagbucks.com'})
    driver.add_cookie({'name' : '__appname', 'value' : 'app2', 'path' : '/', 'domain' : '.swagbucks.com'})
    driver.add_cookie({'name' : '__lp', 'value' : '1', 'path' : '/', 'domain' : '.swagbucks.com'})
    driver.add_cookie({'name' : 'sb5', 'value' : '1', 'path' : '/', 'domain' : '.swagbucks.com'})
    driver.add_cookie({'name' : 'G_ENABLED_IDPS', 'value' : 'google', 'path' : '/', 'domain' : '.www.swagbucks.com'})
    driver.get('http://www.swagbucks.com/')
    while True:
        sleep(2)
    def playVid():
        driver.get('http://www.swagbucks.com/watch/playlists/111/editors-pick')
        driver.find_element_by_class_name('watchCard').click()
        while True:
            try:
                # if any of these are true then we are done
                driver.find_element_by_xpath("//*[contains(text(), 'we are sorry')]")
                return
            except:
                sleep(2)

    while True:
        #main loop
        playVid()

if __name__ == "__main__":
    main()