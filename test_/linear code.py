from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
file_path=r'C:\Users\Lenovo\Downloads\chromedriver_win32\chromedriver.exe'
driver=webdriver.Chrome(file_path)
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
driver.implicitly_wait(50)
time.sleep(2)
#hotel button
driver.find_element("xpath","//span[text()='Hotels']").click()
#search place
driver.find_element("xpath","//input[@id='city']").click()# enter the place
time.sleep(2)
driver.find_element("xpath","//input[@placeholder='Enter city/ Hotel/ Area/ Building']").send_keys("Delhi")#delhi
driver.find_element("xpath","//div[@class='spaceBetween makeFlex hrtlCenter']//p").click()#enter click
time.sleep(2)
driver.find_element("xpath","(//div[@role='gridcell'])[45]").click()#check in
driver.find_element("xpath","(//div[@role='gridcell'])[47]").click()#chek out
#rooms and guest
driver.find_element("xpath","//input[@id='guest']").click()#select room
driver.find_element("xpath",'//div[@class="gstSlct"]').click()#enter no.of rooms
time.sleep(2)
#rooms
driver.find_element("xpath",'//ul[@class="gstSlct__list"]/../..//li[text()="3"]').click()
#adults
driver.find_element("xpath",'//span[@data-testid="adult_count"]').click()
#children
driver.find_element("xpath",'//ul[@class="gstSlct__list"]/../..//li[text()="6"]').click()
driver.find_element("xpath",'//span[@data-testid="children_count"]').click()
time.sleep(2)
driver.find_element("xpath","//li[@class='active']").click()
#apply button
driver.find_element("xpath","//button[text()='Apply']").click()
#cost per day
driver.find_element("xpath","//span[text()='Price per Night']").click()
time.sleep(2)
driver.find_element("xpath",'//li[text()="₹0-₹1500"]').click()
time.sleep(2)
#search button
driver.find_element("xpath","//button[text()='Search']").click()
time.sleep(2)
#enter hotel page
driver.find_element("xpath","//div[@class='flexOne makeFlex']").click()
time.sleep(2)
handles = driver.window_handles
driver.switch_to.window(handles[1])
time.sleep(2)