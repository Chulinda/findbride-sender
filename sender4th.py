from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import turtle
from threading import Thread


screen = turtle.Screen()
screen.title("Find-bride")
screen.bgcolor("purple")
login = screen.textinput("Login", "Enter your login  ")
login = str(login)
password = screen.textinput("Password", "Enter your password  ")
password = str(password)
screen.bye()

def send_in_chat():
    driver = webdriver.Chrome(r'C:\Users\Евгений\Desktop\Bride\chromedriver.exe')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")
    driver.get('http://find-bride.com/girl')
    inputElement = driver.find_element_by_name('form[value1]')
    time.sleep(5)
    inputElement.send_keys(login)
    inputElement = driver.find_element_by_name('form[value2]')
    time.sleep(5)
    inputElement.send_keys(password)
    inputElement.send_keys(Keys.ENTER)
    time.sleep(10)



    SCROLL_PAUSE_TIME = 1

        # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    for _i in range(1):
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            driver.find_element_by_id('more-cards').click()
            continue
        last_height = new_height

    slide_elems = driver.find_elements_by_class_name('start-live-chat')



    x = []
    for elem in slide_elems:
        elem = elem.get_attribute('href')
        elem = str(elem)
        elem = elem.split(",")[0]
        x.append(elem)


    for i in x: 
        i = str(i)
        #print(href)
        time.sleep(3)
        driver.get(i)
        time.sleep(3)
        try:
            inputElement = driver.find_element_by_id("ichat_mess5")
        except:
            pass
        try:
            inputElement.send_keys('Hello')
        except:
            pass
        try:
            inputElement = driver.find_element_by_class_name("fb-btn-red not-ready-to-send icon-outbox")
        except:
            pass
        try:
            inputElement.send_keys(Keys.ENTER)
        except:
            pass

        time.sleep(3)



def send_in_mail():
    driver = webdriver.Chrome(r'C:\Users\Евгений\Desktop\Bride\chromedriver.exe')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")
    driver.get('http://find-bride.com/girl')
    inputElement = driver.find_element_by_name('form[value1]')
    time.sleep(5)
    inputElement.send_keys(login)
    inputElement = driver.find_element_by_name('form[value2]')
    time.sleep(5)
    inputElement.send_keys(password)
    inputElement.send_keys(Keys.ENTER)
    time.sleep(10)



    SCROLL_PAUSE_TIME = 1

        # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    for _i in range(1):
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            driver.find_element_by_id('more-cards').click()
            continue
        last_height = new_height

    slide_elems = driver.find_elements_by_class_name('start-live-chat')

    x = []
    for elem in slide_elems:
        elem = elem.get_attribute('href')
        elem = str(elem)
        elem = elem.split(",")[0]
        x.append(elem)

    ids = []
    for i in x:
        s = i[-7:]
        ids.append(s)


    idprofile = []
    for k in ids:
        link = 'https://find-bride.com/mess/send/all/'+k+'?opened_form=1'
        idprofile.append(link)


    for links in idprofile:
        driver.get(links)
        time.sleep(10)
        try:
            inputElement = driver.find_element_by_id("text2")
        except:
            pass
        try:
            inputElement.send_keys('Hello')
        except:
            pass
        time.sleep(5)
        try:
            inputElement = driver.find_element_by_class_name("button-send-message")
        except:
            pass
        try:
            inputElement.send_keys(Keys.ENTER)
        except:
            pass
        time.sleep(1)
        try:
            inputElement = driver.find_element_by_class_name("fb-btn-red")
        except:
            pass
        try:
            inputElement.send_keys(Keys.ENTER)
        except:
            pass





thread1 = Thread(target=send_in_chat)
thread2 = Thread(target=send_in_mail)

thread1.start()
thread2.start()
thread1.join()
thread2.join()
