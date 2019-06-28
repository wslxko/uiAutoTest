from selenium import webdriver
import read_config
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

config = read_config.ReadConfig()


class Selenium:
    def __init__(self, driver, baseurl):
        self.baseurl = baseurl
        self.driver = driver

    def open_browser(self, num, baseurl):
        self.driver = webdriver.Chrome()
        url = config.read_json(num, baseurl)
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.find_element_by_css_selector('.icon.icon-x').click()

    def waitForShowElement(self, loc):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(*loc))
        except Exception as E:
            return E

    def findElement(self, loc):
        return self.driver.find_element(*loc)

    def isElementExist(self, loc):
        flag = True
        try:
            self.findElement(*loc)
            return flag

        except:
            flag = False
            return flag

# driver = webdriver.Chrome()
# driver.get('https://lauren:MyfUpMNGay@ralphlauren-uat.dev.casaba.tech/')
# driver.find_element_by_css_selector('.icon.icon-x').click()
# addclass1 = "$('.user-pos').addClass('login-show')"
# addclass2 = "$('.user-pos .login').addClass('login-show')"
# driver.execute_script(addclass1)
# driver.execute_script(addclass2)
#
# time.sleep(3)
# driver.find_element_by_css_selector(".login-ipt input[type='tel']").send_keys('17313144673')
# driver.find_element_by_css_selector(".login-ipt input[type='password']").send_keys('LXk141242')
# driver.find_element_by_css_selector(".confirm-button-container .login-tip").click()
#
# a = driver.find_element_by_css_selector(".cafe-toast.cafe-transition-fade.cafe-transition-on").text
#
# time.sleep(3)
# print(a)
