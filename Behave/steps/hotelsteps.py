from behave import *
from selenium import webdriver
import time
@given('I launch browser')
def step_impl(context):
    context.driver=webdriver.Chrome()



@when('I open make my trip')
def step_impl(context):
    context.driver.get("https://www.makemytrip.com/")
    context.driver.maximize_window()
    context.driver.implicitly_wait(50)
    time.sleep(2)




@when('click on hotel')
def step_impl(context):
    context.driver.find_element("xpath","//span[text()='Hotels']").click()



@when(u'click on search and enter name')
def step_impl(context):
    context.driver.find_element("xpath","//input[@id='city']").click()
    time.sleep(2)
    context.driver.find_element("xpath", "//input[@placeholder='Enter city/ Hotel/ Area/ Building']").send_keys("Delhi")


@when(u'click on check-in')
def step_impl(context):
    context.driver.find_element("xpath","//div[@class='spaceBetween makeFlex hrtlCenter']//p").click()
    time.sleep(2)
    context.driver.find_element("xpath","(//div[@role='gridcell'])[45]").click()




@when(u'click on check-out')
def step_impl(context):
    context.driver.find_element("xpath","(//div[@role='gridcell'])[47]").click()



@when(u'click on rooms & guests')
def step_impl(context):
    context.driver.find_element("xpath","//input[@id='guest']").click()#select room
    context.driver.find_element("xpath",'//div[@class="gstSlct"]').click()#enter no.of rooms
    time.sleep(2)



@when(u'select rooms and adults and children')
def step_impl(context):
    context.driver.find_element("xpath",'//ul[@class="gstSlct__list"]/../..//li[text()="3"]').click()
    context.driver.find_element("xpath",'//span[@data-testid="adult_count"]').click()
    context.driver.find_element("xpath",'//ul[@class="gstSlct__list"]/../..//li[text()="6"]').click()
    context.driver.find_element("xpath",'//span[@data-testid="children_count"]').click()
    time.sleep(2)

@when(u'select children age')
def step_impl(context):
    context.driver.find_element("xpath","//li[@class='active']").click()



@when(u'click on apply')
def step_impl(context):
    context.driver.find_element("xpath","//button[text()='Apply']").click()
    context.driver.find_element("xpath", "//span[text()='Price per Night']").click()
    time.sleep(2)
    context.driver.find_element("xpath", '//li[text()="₹0-₹1500"]').click()
    time.sleep(2)

@when(u'I click on search and navigate')
def step_impl(context):
    context.driver.find_element("xpath","//button[text()='Search']").click()
    context.driver.find_element("xpath","//div[@class='flexOne makeFlex']").click()

