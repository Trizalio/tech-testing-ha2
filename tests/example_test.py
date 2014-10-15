import os

import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import Select, WebDriverWait


class ExampleTest(unittest.TestCase):
    def test(self):
        USERNAME = 'tech-testing-ha2-0@bk.ru'
        PASSWORD = os.environ['TTHA2PASSWORD']

        driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX.copy()
        )

        driver.get('https://target.mail.ru/login')

        driver.find_element_by_css_selector('#id_Login').send_keys(USERNAME)
        driver.find_element_by_css_selector('#id_Password').send_keys(PASSWORD)
        select = driver.find_element_by_css_selector('#id_Domain')
        Select(select).select_by_visible_text('@bk.ru')
        driver.find_element_by_css_selector('#gogogo>input').click()

        email = WebDriverWait(driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector('#PH_user-email').text
        )
        self.assertEqual(USERNAME, email)

        driver.quit()
