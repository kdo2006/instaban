import time
from fun.no import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from termcolor import colored
from fun.loader import *

path = "chromedriver"

def reporterboting():
        os.system("clear")
        clickone()
        passwordb = "@reporting.bot50"
        userid = input(colored("Enter victem Username:","yellow"))
        if userid == "kdo_shashank" or userid == "anand_ksri" or userid == "aniket_yadav_91__" or userid == "itz_._samrat__" or userid == "aal.lok123" or userid == "shiprasharma_arts" or userid == "atal_4_s" or userid == "surya_maurya_1729" or userid == "swetaray71" or userid == "kdo_shashank" or userid == "kdo_shashank" or userid == "kdo_shashank" or userid == "kdo_shashank" or userid == "shiprasharma.137" or userid == "cyber.arpan" or userid == "rycoder_1" or userid == "v_4_vivek1":
            print(colored("sale baap ko report kar raha hai..","red"))
            time.sleep(1)
            print(colored("You can't ban this user","red"))
            time.sleep(3)
            reporterboting()
        else:
            time.sleep(3)
            os.system("clear")
            clickone()
            loaderone()
#            firts
            path = "./chromedriver"
            Browser = webdriver.Chrome(path)
            Browser.get('https://www.instagram.com/accounts/login/')
            Browser.implicitly_wait(6)
            usernames = Browser.find_element_by_name("username")
            usernames.send_keys("_bot.___1")
            passwords= Browser.find_element_by_name("password")
            passwords.send_keys(passwordb)
            login= Browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
            login.click()
            nosave = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button")
            nosave.click()
            nonotific = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
            nonotific.click()
            Browser.get("https://www.instagram.com/%s/" % userid)
            Browser.implicitly_wait(5)
            reportone = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[2]/button")
            reportone.click()
            reporttwo = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/button[3]")
            reporttwo.click()
            repoetthree = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/button[2]")
            repoetthree.click()
            reportfour = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/button[1]")
            reportfour.click()
            reportfive = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/button[10]")
            reportfive.click()
            time.sleep(1)
            Browser.quit()
            os.system("clear")
            clickone()
            loadertwo()
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_---_-_-_-
            # second
            path = "./chromedriver"
            Browser = webdriver.Chrome(path)
            Browser.get('https://www.instagram.com/accounts/login/')
            Browser.implicitly_wait(6)
            usernames = Browser.find_element_by_name("username")
            usernames.send_keys("_bot___2")
            passwords= Browser.find_element_by_name("password")
            passwords.send_keys(passwordb)
            login= Browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
            login.click()
            nosave = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button")
            nosave.click()
            nonotific = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
            nonotific.click()
            Browser.get("https://www.instagram.com/%s/" % userid)
            Browser.implicitly_wait(5)
            reportone = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[2]/button")
            reportone.click()
            reporttwo = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/button[3]")
            reporttwo.click()
            repoetthree = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/button[2]")
            repoetthree.click()
            reportfour = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/button[1]")
            reportfour.click()
            reportfive = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/button[10]")
            reportfive.click()
            time.sleep(1)
            Browser.quit()
            os.system("clear")
            clickone()
            loaderthree()
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_---_-_-_-
            #third

            path = "./chromedriver"
            Browser = webdriver.Chrome(path)
            Browser.get('https://www.instagram.com/accounts/login/')
            Browser.implicitly_wait(6)
            usernames = Browser.find_element_by_name("username")
            usernames.send_keys("_bot.___3")
            passwords= Browser.find_element_by_name("password")
            passwords.send_keys(passwordb)
            login= Browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
            login.click()
            nosave = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button")
            nosave.click()
            nonotific = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
            nonotific.click()
            Browser.get("https://www.instagram.com/%s/" % userid)
            Browser.implicitly_wait(5)
            reportone = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[2]/button")
            reportone.click()
            reporttwo = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/button[3]")
            reporttwo.click()
            repoetthree = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/button[2]")
            repoetthree.click()
            reportfour = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/button[1]")
            reportfour.click()
            reportfive = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/button[10]")
            reportfive.click()
            time.sleep(1)
            Browser.quit()
            os.system("clear")
            clickone()
            loaderfour()
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_---_-_-_-
            # fourth
            path = "./chromedriver"
            Browser = webdriver.Chrome(path)
            Browser.get('https://www.instagram.com/accounts/login/')
            Browser.implicitly_wait(6)
            usernames = Browser.find_element_by_name("username")
            usernames.send_keys("_bot.___4")
            passwords= Browser.find_element_by_name("password")
            passwords.send_keys(passwordb)
            login= Browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
            login.click()
            nosave = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button")
            nosave.click()
            nonotific = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
            nonotific.click()
            Browser.get("https://www.instagram.com/%s/" % userid)
            Browser.implicitly_wait(5)
            reportone = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[2]/button")
            reportone.click()
            reporttwo = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/button[3]")
            reporttwo.click()
            repoetthree = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/button[2]")
            repoetthree.click()
            reportfour = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/button[1]")
            reportfour.click()
            reportfive = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/button[10]")
            reportfive.click()
            time.sleep(1)
            Browser.quit()
            os.system("clear")
            clickone()
            loaderfive()

#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_---_-_-_-

            # firts
            path = "./chromedriver"
            Browser = webdriver.Chrome(path)
            Browser.get('https://www.instagram.com/accounts/login/')
            Browser.implicitly_wait(6)
            usernames = Browser.find_element_by_name("username")
            usernames.send_keys("_bot___5")
            passwords= Browser.find_element_by_name("password")
            passwords.send_keys(passwordb)
            login= Browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
            login.click()
            nosave = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button")
            nosave.click()
            nonotific = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
            nonotific.click()
            Browser.get("https://www.instagram.com/%s/" % userid)
            Browser.implicitly_wait(5)
            reportone = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[2]/button")
            reportone.click()
            reporttwo = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/button[3]")
            reporttwo.click()
            repoetthree = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/button[2]")
            repoetthree.click()
            reportfour = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/button[1]")
            reportfour.click()
            reportfive = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/button[10]")
            reportfive.click()
            time.sleep(1)
            Browser.quit()
            os.system("clear")
            clickone()
            loadersix()
        
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_---_-_-_-

            # second
            path = "./chromedriver"
            Browser = webdriver.Chrome(path)
            Browser.get('https://www.instagram.com/accounts/login/')
            Browser.implicitly_wait(6)
            usernames = Browser.find_element_by_name("username")
            usernames.send_keys("_bot.___6")
            passwords= Browser.find_element_by_name("password")
            passwords.send_keys(passwordb)
            login= Browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
            login.click()
            nosave = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button")
            nosave.click()
            nonotific = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
            nonotific.click()
            Browser.get("https://www.instagram.com/%s/" % userid)
            Browser.implicitly_wait(5)
            reportone = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[2]/button")
            reportone.click()
            reporttwo = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/button[3]")
            reporttwo.click()
            repoetthree = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/button[2]")
            repoetthree.click()
            reportfour = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/button[1]")
            reportfour.click()
            reportfive = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/button[10]")
            reportfive.click()
            time.sleep(1)
            Browser.quit()
            os.system("clear")
            clickone()
            loaderseven()

            # bot seven is not working please fix it
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_---_-_-_-
            #third

            path = "./chromedriver"
            Browser = webdriver.Chrome(path)
            Browser.get('https://www.instagram.com/accounts/login/')
            Browser.implicitly_wait(6)
            usernames = Browser.find_element_by_name("username")
            usernames.send_keys("_bot___8")
            passwords= Browser.find_element_by_name("password")
            passwords.send_keys(passwordb)
            login= Browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
            login.click()
            nosave = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button")
            nosave.click()
            nonotific = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
            nonotific.click()
            Browser.get("https://www.instagram.com/%s/" % userid)
            Browser.implicitly_wait(5)
            reportone = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[2]/button")
            reportone.click()
            reporttwo = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/button[3]")
            reporttwo.click()
            repoetthree = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/button[2]")
            repoetthree.click()
            reportfour = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/button[1]")
            reportfour.click()
            reportfive = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/button[10]")
            reportfive.click()
            time.sleep(1)
            Browser.quit()
            os.system("clear")
            clickone()
            loadereight()
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_---_-_-_-
            # fourth
            path = "./chromedriver"
            Browser = webdriver.Chrome(path)
            Browser.get('https://www.instagram.com/accounts/login/')
            Browser.implicitly_wait(6)
            usernames = Browser.find_element_by_name("username")
            usernames.send_keys("_bot.___10")
            passwords= Browser.find_element_by_name("password")
            passwords.send_keys(passwordb)
            login= Browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
            login.click()
            nosave = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button")
            nosave.click()
            nonotific = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
            nonotific.click()
            Browser.get("https://www.instagram.com/%s/" % userid)
            Browser.implicitly_wait(5)
            reportone = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[2]/button")
            reportone.click()
            reporttwo = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/button[3]")
            reporttwo.click()
            repoetthree = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/button[2]")
            repoetthree.click()
            reportfour = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/button[1]")
            reportfour.click()
            reportfive = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/button[10]")
            reportfive.click()
            time.sleep(1)
            Browser.quit()
            os.system("clear")
            clickone()
            loaderenine()

#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_---_-_-_-
            # fourth
            path = "./chromedriver"
            Browser = webdriver.Chrome(path)
            Browser.get('https://www.instagram.com/accounts/login/')
            Browser.implicitly_wait(6)
            usernames = Browser.find_element_by_name("username")
            usernames.send_keys("_bot.___11")
            passwords= Browser.find_element_by_name("password")
            passwords.send_keys(passwordb)
            login= Browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
            login.click()
            nosave = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button")
            nosave.click()
            nonotific = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
            nonotific.click()
            Browser.get("https://www.instagram.com/%s/" % userid)
            Browser.implicitly_wait(5)
            reportone = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[2]/button")
            reportone.click()
            reporttwo = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/button[3]")
            reporttwo.click()
            repoetthree = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/button[2]")
            repoetthree.click()
            reportfour = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/button[1]")
            reportfour.click()
            reportfive = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/button[10]")
            reportfive.click()
            time.sleep(1)
            Browser.quit()
            os.system("clear")
            clickone()
            loaderenine()

            path = "./chromedriver"
            Browser = webdriver.Chrome(path)
            Browser.get('https://www.instagram.com/accounts/login/')
            Browser.implicitly_wait(6)
            usernames = Browser.find_element_by_name("username")
            usernames.send_keys("_bot.___12")
            passwords= Browser.find_element_by_name("password")
            passwords.send_keys(passwordb)
            login= Browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
            login.click()
            nosave = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button")
            nosave.click()
            nonotific = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
            nonotific.click()
            Browser.get("https://www.instagram.com/%s/" % userid)
            Browser.implicitly_wait(5)
            reportone = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[2]/button")
            reportone.click()
            reporttwo = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/button[3]")
            reporttwo.click()
            repoetthree = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/button[2]")
            repoetthree.click()
            reportfour = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/button[1]")
            reportfour.click()
            reportfive = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/button[10]")
            reportfive.click()
            time.sleep(1)
            Browser.quit()
            os.system("clear")
            clickone()
            loaderenine()

            path = "./chromedriver"
            Browser = webdriver.Chrome(path)
            Browser.get('https://www.instagram.com/accounts/login/')
            Browser.implicitly_wait(6)
            usernames = Browser.find_element_by_name("username")
            usernames.send_keys("_bot.___13")
            passwords= Browser.find_element_by_name("password")
            passwords.send_keys(passwordb)
            login= Browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
            login.click()
            nosave = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button")
            nosave.click()
            nonotific = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
            nonotific.click()
            Browser.get("https://www.instagram.com/%s/" % userid)
            Browser.implicitly_wait(5)
            reportone = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[2]/button")
            reportone.click()
            reporttwo = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/button[3]")
            reporttwo.click()
            repoetthree = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/button[2]")
            repoetthree.click()
            reportfour = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/button[1]")
            reportfour.click()
            reportfive = Browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/button[10]")
            reportfive.click()
            time.sleep(1)
            Browser.quit()
            os.system("clear")
            clickone()
            loaderenine()

            
            # ban msg fix
            

