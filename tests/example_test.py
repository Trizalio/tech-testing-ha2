# -*- coding: UTF-8 -*-
import os

import unittest
import urlparse
import random

from selenium.webdriver import ActionChains, DesiredCapabilities, Remote
from selenium.webdriver.support.ui import Select, WebDriverWait

from tests.components import AuthForm, TopMenu
from tests.pages import Page, AuthPage, CreatePage, CampaignsPage
from tests.const import Vars
from time import sleep

class ExampleTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.driver.maximize_window()

        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_page.login()
        pass

    def tearDown(self):
        self.driver.quit()
        pass

    ##done
    def testLogin(self):
        create_page = CreatePage(self.driver)
        create_page.open()

        email = create_page.top_menu.getEmail()
        self.assertEqual(Vars.Login.USERNAME, email)
        pass

    ##done
    def testIncome(self):
        create_page = CreatePage(self.driver)
        create_page.open()

        create_page.whomBlock.income.lock.open()
        create_page.whomBlock.income.low.setChecked()
        create_page.whomBlock.income.medium.setChecked()
        create_page.whomBlock.income.medium.setUnchecked()
        create_page.whomBlock.income.high.setChecked()
        create_page.whomBlock.income.lock.close()
        create_page.whomBlock.income.lock.open()
        self.assertEqual(True, create_page.whomBlock.income.low.getChecked())
        self.assertEqual(False, create_page.whomBlock.income.medium.getChecked())
        self.assertEqual(True, create_page.whomBlock.income.high.getChecked())
        pass


    ##don
    def testCreateBanner(self):
        create_page = CreatePage(self.driver)
        create_page.open()


        baseStats = create_page.BaseStats
        baseStats.companyProduct.setProductTypeGame()
        baseStats.companyTarget.setTargetMyWorld()
        baseStats.setCompanyName(Vars.BaseStats.NAME)


        create_page.formBlock.title.setText(Vars.MainStats.TITLE)
        create_page.formBlock.text.setText(Vars.MainStats.TEXT)
        create_page.formBlock.link.setText(Vars.MainStats.LINK)
        create_page.formBlock.imageGrabber.setImage(Vars.MainStats.IMAGE)

        #result =  WebDriverWait(self.driver, 10, 0.5).until(
        #    lambda d: create_page.formBlock.imagePreview.getImageUrl() is not None
        #)
        sleep(2)

        create_page.formBlock.submit.click()
        
        self.assertEqual(Vars.MainStats.TITLE, create_page.bannerPreview.title.getText())
        self.assertEqual(Vars.MainStats.TEXT, create_page.bannerPreview.text.getText())
        self.assertIsNotNone(create_page.bannerPreview.image.getImageUrl())
        pass

    ##done
    def testWhenTime(self):
        create_page = CreatePage(self.driver)
        create_page.open()

        create_page.whenBlock.timeBlock.lock.open()
        create_page.whenBlock.timeBlock.workTime.click()
        self.assertEqual(Vars.Time.WORK_TIME, create_page.whenBlock.timeBlock.text.getText())
        create_page.whenBlock.timeBlock.monday0.open()
        self.assertEqual(Vars.Time.HOURS_56, create_page.whenBlock.timeBlock.text.getText())
        pass

    ##done
    def testCreateCompany(self):
        create_page = CreatePage(self.driver)
        create_page.open()

        baseStats = create_page.BaseStats
        baseStats.companyProduct.setProductTypeGame()
        baseStats.companyTarget.setTargetMyWorld()
        baseStats.setCompanyName(Vars.BaseStats.NAME)

        create_page.formBlock.title.setText(Vars.MainStats.TITLE)
        create_page.formBlock.text.setText(Vars.MainStats.TEXT)
        create_page.formBlock.link.setText(Vars.MainStats.LINK)
        create_page.formBlock.imageGrabber.setImage(Vars.MainStats.IMAGE)

        sleep(2)
        create_page.formBlock.submit.click()

        sleep(2)
        create_page.footerBlock.submit.click()

        compaign_page = CampaignsPage(self.driver)
        compaign_page.open()

        self.assertEqual(Vars.BaseStats.NAME, compaign_page.compaignsList.compaign.compaignName.getText())
        self.assertEqual(Vars.MainStats.TEXT, compaign_page.compaignsList.compaign.text.getText())
        self.assertEqual(Vars.MainStats.TITLE, compaign_page.compaignsList.compaign.title.getText())
        self.assertIsNotNone(compaign_page.compaignsList.compaign.image.getImageUrl())
