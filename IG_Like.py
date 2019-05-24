#Arleigh Chang
#For 2019/3/23 IG Version


from selenium import webdriver
import time


driver = webdriver.Chrome()

#Here is target URL
driver.get('https://www.instagram.com/jaychou/?hl=zh-tw')
driver.find_element_by_xpath("//a[@class='tdiEy']/button").click()
driver.get(driver.current_url)



#''''''''''''''''''''''''''''''''''''[Here choose your Login way]''''''''''''''''''''''''''''
#==============================[1]NORMAL IG LOGIN===========================================

try:
    driver.find_element_by_name('username').send_keys("Yourusername")

    driver.find_element_by_name('password').send_keys("Yourpassword")

    driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[4]/button/div").click()
except:
    print('Login Error')

#==============================[2]FACEBOOK LOGIN===========================================

# driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[5]/button").click()
# try:
#     driver.find_element_by_xpath("//*[@id='email']").send_keys("YourFacebookusername")

#     driver.find_element_by_xpath("//*[@id='pass']").send_keys("YourFacebookpassword")

#     driver.find_element_by_xpath("//*[@id='loginbutton']").click()
# except:
#     print('Login Error')




driver.implicitly_wait(10)
driver.switch_to_window(driver.window_handles[-1])

time_start=time.time()


driver.find_element_by_xpath("//div[@class = '_9AhH0']").click()
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/article/div[2]/section[1]/span[1]/button").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/a").click()

for i in range(0,10000):  
    try:
        driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/a[2]").click()
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/article/div[2]/section[1]/span[1]/button").click()
        time.sleep(0.5)
    except:
        time_end=time.time()
        print('time cost',time_end-time_start,'s')
        break

