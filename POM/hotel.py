import time
import pytest
#from selenium import webdriver
from LIBRARY.config import Config
from DATA import reading_objects

#driver = webdriver.Chrome(r'C:\Users\Lenovo\Downloads\chromedriver_win32\chromedriver.exe')


lo_obj = reading_objects.read_locators()
class Search:
    # locators = read_locators("data")
    def __init__(self,driver):
        self.driver=driver

    def search_place(self):
        self.driver.find_element(*lo_obj['hotel_button']).click()
        time.sleep(2)
        self.driver.find_element(*lo_obj['Search _hotel _type']).click()
        time.sleep(2)
        self.driver.find_element(*lo_obj['Search_place']).send_keys('Delhi')
        time.sleep(2)
        self.driver.find_element(*lo_obj['Select_hotel']).click()
        time.sleep(2)
    def checkin_date(self):
        self.driver.find_element(*lo_obj['Check_in']).click()
        time.sleep(2)
    def checkout_date(self):
        self.driver.find_element(*lo_obj['Check_out']).click()
        time.sleep(2)
    def rooms_guests(self):
        self.driver.find_element(*lo_obj['Rooms_Guests']).click()
        time.sleep(2)
        self.driver.find_element(*lo_obj['Adults']).click()
        time.sleep(2)
        self.driver.find_element(*lo_obj['Children']).click()
        time.sleep(2)
        self.driver.find_element(*lo_obj['Adults_count']).click()
        time.sleep(2)
        self.driver.find_element(*lo_obj['Select_adults_age']).click()
        time.sleep(2)
        self.driver.find_element(*lo_obj['Search_children']).click()
        time.sleep(2)
        self.driver.find_element(*lo_obj['Select_age']).click()
        time.sleep(2)
    def apply(self):
        self.driver.find_element(*lo_obj['Apply_button']).click()
        time.sleep(2)

    def price_per_night(self):
        self.driver.find_element(*lo_obj['Price_per_night']).click()
        time.sleep(2)
        self.driver.find_element(*lo_obj['Select_cost']).click()
        time.sleep(2)
        self.driver.find_element(*lo_obj['Select_button']).click()
        time.sleep(2)
    def search(self):
        self.driver.find_element(*lo_obj['Enter_city']).click()

# lp = Search(driver)
# lp.select_hotel()
# lp.search_place()
# lp.checkin_date()
# lp.checkout_date()
# lp.rooms_guests()
# lp.apply()
# lp.price_per_night()
# lp.search()



