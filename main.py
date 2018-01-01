from selenium import webdriver
from time import sleep

options = webdriver.ChromeOptions()

#options.add_argument('headless')

driver = webdriver.Chrome(chrome_options=options)


driver.get('https://www.swagbucks.com/p/login')

## wait for user to login
while "Login" in driver.title:
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