from pageObject.login_page import PageObject
import time


class Login(PageObject):
    def login(self, username, password):
        self.login_show()
        time.sleep(2)
        self.send_username(username)
        self.send_password(password)
        self.click_btn()
