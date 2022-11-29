import pytest
import time
# from DATA import reading_objects
from POM.hotel import Search


class TestSearch:
    def test_hotel(self,init_driver):
        driver = init_driver
        lp = Search(driver)
        # lp.select_hotel()
        lp.search_place()
        lp.checkin_date()
        lp.checkout_date()
        lp.rooms_guests()
        lp.apply()
        lp.price_per_night()
        lp.search()

