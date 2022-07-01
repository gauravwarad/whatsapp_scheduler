from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os

ip_date_time = "20-04-2021 23:33:00"
#ip_dt = input("enter the date in format dd-mm-yyyy:\n")
#ip_time = input("enter the time in format hh:mm:ss (please use 24hr format)\n")
#ip_date_time = ip_dt + " " + ip_time
#ip_msg = input("enter the message to send")


ip_date_time_obj = time.strptime(ip_date_time, "%d-%m-%Y %H:%M:%S")

time1 = time.mktime(ip_date_time_obj)

print(time1)

time_to_sleep = time1 - time.time()

#print(time_to_sleep)

print("going to sleep for ",time_to_sleep)

#time.sleep(time_to_sleep)
print("sleep time is over")


#contact = "Popu"
text = "automated msg(pls ignore)"


options = webdriver.ChromeOptions()
#todo: change gaurav to username
options.add_argument("user-data-dir=C:\\Users\\Gaurav\\AppData\\Local\\Google\\Chrome\\User Data")
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://web.whatsapp.com")

#todo change it to 60
time.sleep(10)

#inp_xpath_search = "//input[@title='Search or start new chat']"
#button xpath /html/body/div[1]/div/div/div[3]/div/div[1]/div/button


search_button_xpath = "/html/body/div[1]/div[1]/div[1]/div[3]/div/div[1]/div/button"

search_box = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(search_button_xpath))
search_box.click()

inp_xpath_search = "/html/body/div[1]/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]"
# "/html/body/div[1]/div/div/div[3]/div/div[1]/div/div "

#content = driver.find_element_by_class_name('')

input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
input_box_search.click()
time.sleep(2)
input_box_search.send_keys("Rushikesh")
time.sleep(20)
top_contact_xpath = "/html/body/div[1]/div[1]/div[1]/div[3]/div/div[2]/div[1]/div/div/div[10]"
#    "/html/body/div[1]/div[1]/div[1]/div[3]/div/div[2]/div[1]/div/div/div[10]/div"
#
#/html/body/div[1]/div[1]/div[1]/div[3]/div/div[2]/div[1]/div/div/div[12]
#top_contact_xpath = "/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[1]"
contact_box = driver.find_element_by_xpath(top_contact_xpath)
contact_box.click()

print("searching contact")

#selected_contact = driver.find_element_by_xpath("//span[@title='"+contact+"']")
#selected_contact.click()

inp_xpath = "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]"
#/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div
#'//div[@class="_2S1VP copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'
input_box = driver.find_element_by_xpath(inp_xpath)
time.sleep(2)
#input_box.send_keys(text + Keys.ENTER)

print("message sent")
time.sleep(5)

driver.quit()



time.sleep(10)
#os.system("shutdown /s /t 1")