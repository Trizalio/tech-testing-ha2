# -*- coding: UTF-8 -*-
import urlparse
#from tests.components import AuthForm, TopMenu, Slider, TimeSelector, BaseCampaignSettings, AdsForm, Gender
from tests.components import AuthForm, TopMenu, BaseAdStats, FormBlock, WhomBlock, BannerPreview, FooterBlock, WhenBlock, CompaignsList, waitAndFind2
from tests.const import Vars

#from selenium.webdriver.support.wait import WebDriverWait


class Page(object):
    BASE_URL = 'https://target.mail.ru'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver


    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        print "opened"
        WebDriverWait(driver, 1, 3).until(
           lambda d: True
        )
        print "waited"


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
        return AuthForm(self.driver)

class CampaignsPage(Page):
    PATH = '/ads/campaigns'

    COMPAIGNS = 'ul[class="campaigns-page__campaigns js-campaigns-wrapper"]'

    @property
    def compaignsList(self):
        if not hasattr(self, '__compaignsListInitDone'):
            setattr(self, '__compaignsList', CompaignsList(waitAndFind2(self.driver, self.COMPAIGNS)))
            setattr(self, '__compaignsListInitDone', True)
        return getattr(self, '__compaignsList')


class CreatePage(Page):
    PATH = '/ads/create'

    WHOM = 'div[data-name="whom"]'
    FORM = 'div[class="banner-form"]'
    PREVIEW = 'li[class="added-banner"]'
    FOOTER = 'div[class="create-page__footer"]'
    WHEN ='div[data-name="when"]'

    @property
    def top_menu(self):
        return TopMenu(self.driver)

    @property
    def BaseStats(self):
        return BaseAdStats(self.driver)

    @property
    def formBlock(self):
        if not hasattr(self, '__formBlockInitDone'):
            setattr(self, '__formBlock', FormBlock(waitAndFind2(self.driver, self.FORM)))
            setattr(self, '__formBlockInitDone', True)
        return getattr(self, '__formBlock')

    @property
    def whomBlock(self):
        if not hasattr(self, '__whomBlockInitDone'):
            setattr(self, '__whomBlock', WhomBlock(waitAndFind2(self.driver, self.WHOM)))
            setattr(self, '__whomBlockInitDone', True)
        return getattr(self, '__whomBlock')

    @property
    def bannerPreview(self):
        if not hasattr(self, '__bannerPreviewInitDone'):
            setattr(self, '__bannerPreview', BannerPreview(waitAndFind2(self.driver, self.PREVIEW)))
            setattr(self, '__bannerPreviewInitDone', True)
        return getattr(self, '__bannerPreview')

    @property
    def whenBlock(self):
        if not hasattr(self, '__whenBlockInitDone'):
            setattr(self, '__whenBlock', WhenBlock(waitAndFind2(self.driver, self.WHEN)))
            setattr(self, '__whenBlockInitDone', True)
        return getattr(self, '__whenBlock')

        

    @property
    def footerBlock(self):
        if not hasattr(self, '__footerBlockInitDone'):
            setattr(self, '__footerBlock', FooterBlock(waitAndFind2(self.driver, self.FOOTER)))
            setattr(self, '__footerBlockInitDone', True)
        return getattr(self, '__footerBlock')
