from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
class WebPage:
    def __init__(self, web_module):
        self.web_module=web_module
        
    def wait_for_element(self, css_selector: str, timeout=5):
        return WebDriverWait(self.web_module.driver, timeout=timeout).until(lambda d: d.find_element(By.CSS_SELECTOR, css_selector))
        
    def switch_to_window(self, window_handle):
        self.web_module.driver.switch_to.window(window_handle)
 

class PersonalPage(WebPage):
    def get_real_username(self, timeout=5):
        user_name_div = self.wait_for_element("div.personalHeader__info__col-detail div:first-child", timeout)
        return user_name_div.text
        
    def click_logout_btn(self, timeout=5):
        logout_btn = self.wait_for_element('a[href="//login.104.com.tw/logout"]', timeout)
        logout_btn.click()


class LoginPage(WebPage):
    def fill_username(self, username: str, timeout=3):
        username_textfield = self.wait_for_element("#username", timeout)
        username_textfield.send_keys(username)
        
    def fill_password(self, password: str, timeout=3):
        password_textfield = self.wait_for_element("#password", timeout)
        password_textfield.send_keys(password)
        
    def click_login_btn(self, timeout=3):
        login_btn = self.wait_for_element("#submitBtn", timeout)
        login_btn.click()
        return MainPage(self.web_module)
 

class MainPage(WebPage):
    def skip_popup(self, timeout=5):
        close_btn = self.wait_for_element(".btn.btn-sm.btn-outline-secondary.mr-4", timeout)
        close_btn.click()

    def click_login(self, timeout=3):
        login_btn = self.wait_for_element("li.right ul.global_nav a[onclick^=login_get]", timeout)
        login_btn.click()
        return LoginPage(self.web_module)
    
    def click_name_btn(self, timeout=5):
        name_btn = self.wait_for_element("#name_link", timeout)
        name_btn.click()
        
    def click_member_center_btn(self, timeout=5):
        original_window = self.web_module.driver.current_window_handle
        member_center_btn = self.wait_for_element("div.personal_box dl.myfamilychannel dt:first-child a[onclick]", timeout)
        member_center_btn.click()
        WebDriverWait(self.web_module.driver, 10).until(EC.number_of_windows_to_be(2))
        for window_handle in self.web_module.driver.window_handles:
            if window_handle != original_window:
                self.switch_to_window(window_handle)
        return PersonalPage(self.web_module)
        

