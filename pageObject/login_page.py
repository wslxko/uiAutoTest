from common.selenium_tools import Selenium
from selenium.webdriver.common.by import By


class PageObject(Selenium):
    username_loc = (By.CSS_SELECTOR, ".login-ipt input[type='tel']")
    password_loc = (By.CSS_SELECTOR, ".login-ipt input[type='password']")
    loginBtn_loc = (By.CSS_SELECTOR, ".confirm-button-container .login-tip")
    addclass1 = "$('.user-pos').addClass('login-show')"
    addclass2 = "$('.user-pos .login').addClass('login-show')"
    assert_loc = (By.CSS_SELECTOR, ".cafe-toast.cafe-transition-fade.cafe-transition-on")
    search_loc = (By.CSS_SELECTOR, '.search')
    searchAssert_loc = (By.ID, 'keyword')
    scroll_js = "var q = document.documentElement.scrollTop = 100000"
    assert_bottom_loc = (By.CSS_SELECTOR, '.confirm-button-page')

    def login_show(self):
        self.driver.execute_script(self.addclass1)
        self.driver.execute_script(self.addclass2)

    def send_username(self, username):
        ele = self.findElement(self.username_loc)
        ele.clear()
        ele.send_keys(username)

    def send_password(self, password):
        ele = self.findElement(self.password_loc)
        ele.clear()
        ele.send_keys(password)

    def click_btn(self):
        ele = self.findElement(self.loginBtn_loc)
        ele.click()

    def assert_text(self):
        ele = self.findElement(self.assert_loc)
        return ele.text

    def click_search(self):
        ele = self.findElement(self.search_loc)
        ele.click()

    def search_assert(self):
        ele = self.findElement(self.searchAssert_loc)
        return ele

    def scroll_bottom(self):
        return self.driver.execute_script(self.scroll_js)

    def assert_bottom(self):
        ele = self.findElement(self.assert_bottom_loc)
        return ele.text
