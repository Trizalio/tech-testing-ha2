# -*- coding: UTF-8 -*-
import urlparse
#from tests.components import AuthForm, TopMenu, Slider, TimeSelector, BaseCampaignSettings, AdsForm, Gender
from tests.components import AuthForm, TopMenu, BaseAdStats, FormBlock, WhomBlock, BannerPreview, FooterBlock, WhenBlock, CompaignsList, waitAndFind2
from tests.components import createOnFirstAccess, invalidateFunction
from tests.const import Vars
from time import sleep


#from selenium.webdriver.support.wait import WebDriverWait


class Page(object):
    BASE_URL = 'https://target.mail.ru'
    PATH = ''

    def __init__(self, driver):
        self.element = driver


    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.element.get(url)


class AuthPage(Page):
    PATH = '/login'

    def login(self):
        auth_form = self.form
        auth_form.setDomain(Vars.Login.DOMAIN)
        auth_form.setLogin(Vars.Login.USERNAME)
        auth_form.setPassword(Vars.Login.PASSWORD)
        auth_form.submit()
        pass

    @property
    def form(self):
        return AuthForm(self.element)

class CampaignsPage(Page):
    PATH = '/ads/campaigns'

    COMPAIGNS = 'ul[class="campaigns-page__campaigns js-campaigns-wrapper"]'

    @property
    def compaignsList(self):
        return createOnFirstAccess(self, "compaignsList", CompaignsList, self.COMPAIGNS)


class CreatePage(Page):
    PATH = '/ads/create'

    WHOM = 'div[data-name="whom"]'
    FORM = 'div[class="banner-form"]'
    PREVIEW = 'li[class="added-banner"]'
    FOOTER = 'div[class="create-page__footer"]'
    WHEN ='div[data-name="when"]'

    @property
    def top_menu(self):
        return TopMenu(self.element)

    @property
    def BaseStats(self):
        return BaseAdStats(self.element)

    @property
    def formBlock(self):
        return createOnFirstAccess(self, "formBlock", FormBlock, self.FORM)

    @property
    def whomBlock(self):
        return createOnFirstAccess(self, "whomBlock", WhomBlock, self.WHOM)

    @property
    def bannerPreview(self):
        return createOnFirstAccess(self, "bannerPreview", BannerPreview, self.PREVIEW)

    @property
    def whenBlock(self):
        return createOnFirstAccess(self, "whenBlock", WhenBlock, self.WHEN)

    @property
    def footerBlock(self):
        return createOnFirstAccess(self, "footerBlock", FooterBlock, self.FOOTER)
