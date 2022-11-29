# import time
# import pytest
# from selenium import webdriver
# from LIBRARY.config import Config
# # path = r"C:\Users\Mohite's\Downloads\chromedriver_win32\chromedriver.exe"
# # from webdriver_manager.microsoft import EdgeChromiumDriverManager
# # from webdriver_manager.firefox import GeckoDriverManager
# # from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.firefox.options import Options
#
# #Cross Browsing
# firefox_Driver_path = r'C:\Users\Lenovo\Downloads\chromedriver_win32\geckodriver.exe'
# @pytest.fixture(params=["Firefox","Edge","Chrome"])
# def _driver(request):
#
#
#
#
#     if request.param == "Firefox":
#         options = Options()
#         options.binary_location= r'C:\Program Files\Mozilla Firefox\firefox.exe'
#         driver = webdriver.Firefox(executable_path=firefox_Driver_path,options=options)
#
#
#     elif request.param == "Edge":
#         driver = webdriver.Edge(Config.Edge_Driver_Path)
#
#
#
#     elif request.param == "Chrome":
#         driver = webdriver.Chrome(Config.Chrome_Driver_path)
#
#
#
#     driver.get(Config.URL)
#     driver.maximize_window()
#     yield driver
#     print(driver.title)
#     # driver.save_screenshot("text_loginpage.png")
#     driver.close()





import time
import pytest
from selenium import webdriver
from LIBRARY.config import Config
from selenium.webdriver.firefox.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
path = r"C:\Users\Lenovo\Downloads\chromedriver_win32\geckodriver.exe"


#Cross Browsing
@pytest.fixture(params=["Chrome","Edge",])
def init_driver(request):


    if request.param == "Chrome":
        driver = webdriver.Chrome(Config.Chrome_Driver_path)

    elif request.param == "Edge":
        driver = webdriver.Edge(Config.Edge_Driver_path)

    # elif request.param == "Firefox":
    #     option = Options()
    #     option.binary_location =r'C:\Progrm Files\Mozilla Firefox\firefox.exe'
    #     driver = webdriver.Firefox(executable_path=path, options=option)

    driver.get(r"https://www.makemytrip.com/")
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield driver
    driver.save_screenshot(Config.Screen_shots_path+'hotel.png')
    driver.close()