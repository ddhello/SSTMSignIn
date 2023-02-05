import time
import schedule
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

firstrun = True
def reply():
    print("开始执行任务...")
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach",True)
    driver = webdriver.Chrome(executable_path= "chromedriver.exe",options= option)
    wait = WebDriverWait(driver,2000)
    driver.get("https://sstm.moe/forum/72-同盟签到区")
    Xpath_temp = '//*[@id="elUserSignIn"]'
    menu = driver.find_element(by=By.XPATH,value = Xpath_temp)
    menu.click()
    Xpath_temp = '//*[@id="elUserSignIn_menu"]/form/div/div/ul/li[1]/input'
    username = driver.find_element(by=By.XPATH,value=Xpath_temp)
    username.send_keys("在这里输入邮箱")
    Xpath_temp = '//*[@id="elUserSignIn_menu"]/form/div/div/ul/li[2]/input'
    password = driver.find_element(by=By.XPATH,value=Xpath_temp)
    password.send_keys("在这里输入密码")
    Xpath_temp = '//*[@id="elSignIn_submit"]'
    sumbit = driver.find_element(by=By.XPATH,value=Xpath_temp)
    sumbit.click()
    threads = driver.find_elements(by=By.CLASS_NAME,value="ipsContained")
    link = threads[0].find_element(by=By.TAG_NAME,value="a")
    link.click()
    Xpath_temp = '//*[@id="ipsLayout_mainArea"]/div[3]/ul/li/span/a'
    reply = driver.find_element(by= By.XPATH,value = Xpath_temp)
    reply.click()
    time.sleep(0.5)
    reply_content = driver.find_element(by=By.CLASS_NAME,value = 'cke_wysiwyg_div')
    times = time.time()
    local_time = time.localtime(times)
    time_formated = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    reply_content.send_keys(time_formated)
    driver.find_element(by=By.XPATH,value='//*[@id="comments"]/div[5]/form/div/div[3]/ul/li[2]/button').click()
    print("任务执行完成")
    driver.close()

schedule.every().day.at("00:30").do(reply)
if firstrun:
    reply()
while True:
    schedule.run_pending()
    time.sleep(30)