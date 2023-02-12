import unittest
from webTestModule import WebModule
from webpage import MainPage, LoginPage, PersonalPage
from config import username, password, expected_real_username
import time

class Test104JobSearch(unittest.TestCase):
    def setUp(self):
        self.web_module = WebModule()
        
    def test_login(self):
        main_page = MainPage(self.web_module)
        main_page.skip_popup()
        login_page: LoginPage = main_page.click_login()
        login_page.fill_username(username)
        login_page.fill_password(password)
        main_page = login_page.click_login_btn()
        main_page.click_name_btn()
        personal_page: PersonalPage = main_page.click_member_center_btn()
        real_username = personal_page.get_real_username()
        self.assertEqual(real_username, expected_real_username)
        personal_page.click_logout_btn()
        
    def tearDown(self):
        self.web_module.close()