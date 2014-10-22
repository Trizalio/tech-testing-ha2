
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions
#from selenium.webdriver.common.keys import Keys
#from datetime import datetime
#from tests.page_objects.Const import Const


from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from tests.atoms import Element, ImageGrabber, Image, Button, Text, Textbox, Radiobutton, Groupbox, Checkbox

class Component(object):
    def __init__(self, driver):
        self.driver = driver


def waitAndFindbyClass(driver, targetName):
    result =  WebDriverWait(driver, 30, 0.1).until(
        lambda d: d.find_element_by_class_name(targetName)
    )
    for target in result:
        if target.is_displayed():
            return target
    pass


def waitAndFind2(driver, targetName):
    result =  WebDriverWait(driver, 30, 0.1).until(
       lambda d: d.find_elements_by_css_selector(targetName)
    )
    for target in result:
       print target

    result =  WebDriverWait(driver, 6, 0.5).until(
        lambda d: d.find_element_by_css_selector(targetName)
    )
    return result

def waitAndFind(driver, targetName):
    result =  WebDriverWait(driver, 30, 0.1).until(
        lambda d: d.find_elements_by_css_selector(targetName)
    )
    for target in result:
        if target.is_displayed():
            return target
    pass

def waitAndFindAndFillTextField(driver, targetName, text):
    result = waitAndFind(driver, targetName)
    result.clear()
    result.send_keys(text)
    pass

def waitAndFindAndGetChecked(driver, targetName):
    result = waitAndFind(driver, targetName)
    return result.is_selected()

def waitAndFindAndSetChecked(driver, targetName, state):
    result = waitAndFind(driver, targetName)
    if result.is_selected() != state:
        result.click()
    pass


class AuthForm(Component):
    LOGIN = '#id_Login'
    PASSWORD = '#id_Password'
    DOMAIN = '#id_Domain'
    SUBMIT = '#gogogo>input'

    def setLogin(self, login):
        waitAndFind(self.driver, self.LOGIN).send_keys(login)
        pass

    def setPassword(self, password):
        waitAndFind(self.driver, self.PASSWORD).send_keys(password)
        pass

    def setDomain(self, domain):
        target = waitAndFind(self.driver, self.DOMAIN)
        Select(target).select_by_visible_text(domain)
        pass

    def submit(self):
        waitAndFind(self.driver, self.SUBMIT).click()
        pass



class TopMenu(Component):
    EMAIL = '#PH_user-email'

    def getEmail(self):
        result = waitAndFind(self.driver, self.EMAIL).text
        return result




class Product(Component):
    GAME = 'input[id="product-type-5208"]'

    def setProductTypeGame(self):
        waitAndFind(self.driver, self.GAME).click()

class Target(Component):
    MYWORLD = '#pad-mail_mir_abstract'
    def setTargetMyWorld(self):
        waitAndFind(self.driver, self.MYWORLD).click()

class BaseAdStats(Component):
    NAME = '.base-setting__campaign-name__input'

    def setCompanyName(self, name):
        waitAndFindAndFillTextField(self.driver, self.NAME, name)
        pass

    @property
    def companyProduct(self):
        return Product(self.driver)

    @property
    def companyTarget(self):
        return Target(self.driver)



class FormBlock(Element):
    TITLE = 'input[data-name="title"]'
    TEXT = 'textarea[data-name="text"]'
    LINK = 'li[style="display: list-item;"] input[data-name="url"]'
    SUBMIT = 'input[type="submit"]'
    IMAGE_GRABBER = 'input[data-name="image"]'
    IMAGE_PREVIEW = 'span[class="banner-preview__img"]'


    @property
    def title(self):
        if not hasattr(self, '__titleDone'):
            setattr(self, '__title', Textbox(waitAndFind2(self.element, self.TITLE)))
            setattr(self, '__titleInitDone', True)
        return getattr(self, '__title')

    @property
    def text(self):
        if not hasattr(self, '__textDone'):
            setattr(self, '__text', Textbox(waitAndFind2(self.element, self.TEXT)))
            setattr(self, '__textInitDone', True)
        return getattr(self, '__text')

    @property
    def link(self):
        if not hasattr(self, '__linkDone'):
            setattr(self, '__link', Textbox(waitAndFind2(self.element, self.LINK)))
            setattr(self, '__linkInitDone', True)
        return getattr(self, '__link')

    @property
    def submit(self):
        if not hasattr(self, '__submitDone'):
            setattr(self, '__submit', Button(waitAndFind2(self.element, self.SUBMIT)))
            setattr(self, '__submitInitDone', True)
        return getattr(self, '__submit')

    @property
    def imageGrabber(self):
        if not hasattr(self, '__imageGrabberDone'):
            setattr(self, '__imageGrabber', ImageGrabber(waitAndFind2(self.element, self.IMAGE_GRABBER)))
            setattr(self, '__imageGrabberInitDone', True)
        return getattr(self, '__imageGrabber')

    @property
    def image(self):
        if not hasattr(self, '__imageDone') or getattr(self, '__imageDone') == False:
            setattr(self, '__image', Image(waitAndFind2(self.element, self.IMAGE_PREVIEW)))
            setattr(self, '__imageInitDone', True)
        return getattr(self, '__image')

class Income(Element):
    LOW = 'input[id="income_group-9286"]'
    MEDIUM = 'input[id="income_group-9287"]'
    HIGH = 'input[id="income_group-9288"]'
    LOCK = 'div[data-name="income_group"] span[class*="campaign-setting__value"]'

    @property
    def lock(self):
        if not hasattr(self, '__lockInitDone'):
            print "lock"
            setattr(self, '__lock', Groupbox(waitAndFind2(self.element, self.LOCK)))
            setattr(self, '__lockInitDone', True)
        return getattr(self, '__lock')

    @property
    def low(self):
        if not hasattr(self, '__lowInitDone'):
            setattr(self, '__low', Checkbox(waitAndFind2(self.element, self.LOW)))
            setattr(self, '__lowInitDone', True)
        return getattr(self, '__low')

    @property
    def medium(self):
        if not hasattr(self, '__mediumInitDone'):
            setattr(self, '__medium', Checkbox(waitAndFind2(self.element, self.MEDIUM)))
            setattr(self, '__mediumInitDone', True)
        return getattr(self, '__medium')

    @property
    def high(self):
        if not hasattr(self, '__highInitDone'):
            setattr(self, '__high', Checkbox(waitAndFind2(self.element, self.HIGH)))
            setattr(self, '__highInitDone', True)
        return getattr(self, '__high')

class WhomBlock(Element):

    INCOME_GROUP = 'li[data-name="income_group"]'

    @property
    def income(self):
        if not hasattr(self, '__incomeInitDone'):
            setattr(self, '__income', Income(waitAndFind2(self.element, self.INCOME_GROUP)))
            setattr(self, '__incomeInitDone', True)
        return getattr(self, '__income')

class BannerPreview(Element):
    TITLE = 'span[class="banner-preview__title"]'
    TEXT = 'p[class="banner-preview__text"]'
    IMAGE = 'span[class="banner-preview__img"]'

    @property
    def title(self):
        if not hasattr(self, '__titleInitDone'):
            setattr(self, '__title', Text(waitAndFind2(self.element, self.TITLE)))
            setattr(self, '__titleInitDone', True)
        return getattr(self, '__title')

    @property
    def text(self):
        if not hasattr(self, '__textInitDone'):
            setattr(self, '__text', Text(waitAndFind2(self.element, self.TEXT)))
            setattr(self, '__textInitDone', True)
        return getattr(self, '__text')

    @property
    def image(self):
        if not hasattr(self, '__imageInitDone'):
            setattr(self, '__image', Image(waitAndFind2(self.element, self.IMAGE)))
            setattr(self, '__imageInitDone', True)
        return getattr(self, '__image')

class WhenBlock(Element):
    TIME = 'li[data-name="fulltime"]'

    @property
    def timeBlock(self):
        if not hasattr(self, '__timeBlockInitDone'):
            setattr(self, '__timeBlock', TimeBlock(waitAndFind2(self.element, self.TIME)))
            setattr(self, '__timeBlockInitDone', True)
        return getattr(self, '__timeBlock')

class TimeBlock(Element):
    BUTTON_WORKTIME = 'li[data-name="workTime"]'
    LOCK = 'div[data-name="fulltime"] span[class*="campaign-setting__value"]'
    CHECKBOX_MONDAY_0 = 'ul[data-name="mon"] li[data-id="0"]'

    @property
    def workTime(self):
        if not hasattr(self, '__workTimeInitDone'):
            setattr(self, '__workTime', Button(waitAndFind2(self.element, self.BUTTON_WORKTIME)))
            setattr(self, '__workTimeInitDone', True)
        return getattr(self, '__workTime')

    @property
    def monday0(self):
        if not hasattr(self, '__monday0InitDone'):
            setattr(self, '__monday0', Groupbox(waitAndFind2(self.element, self.CHECKBOX_MONDAY_0)))
            setattr(self, '__monday0InitDone', True)
        return getattr(self, '__monday0')

    @property
    def lock(self):
        if not hasattr(self, '__lockInitDone'):
            setattr(self, '__lock', Groupbox(waitAndFind2(self.element, self.LOCK)))
            setattr(self, '__lockInitDone', True)
        return getattr(self, '__lock')

    @property
    def text(self):
        if not hasattr(self, '__textInitDone'):
            setattr(self, '__text', Text(waitAndFind2(self.element, self.LOCK)))
            setattr(self, '__textInitDone', True)
        return getattr(self, '__text')


class FooterBlock(Element):
    BUTTON = 'span[class="main-button__label"]'

    @property
    def submit(self):
        if not hasattr(self, '__submitInitDone'):
            setattr(self, '__submit', Button(waitAndFind2(self.element, self.BUTTON)))
            setattr(self, '__submitInitDone', True)
        return getattr(self, '__submit')
#////////////////////////////////////////////////////////////////////////////////////////////////////////////

class CompaignsList(Element):
    LAST_COMPAIGN = 'li[class="campaign-row"]'

    @property
    def compaign(self):
        if not hasattr(self, '__compaignInitDone'):
            setattr(self, '__compaign', Compaign(waitAndFind2(self.element, self.LAST_COMPAIGN)))
            #setattr(self, '__compaign', Compaign(self.element))
            setattr(self, '__compaignInitDone', True)
        return getattr(self, '__compaign')

class Compaign(Element):
    COMPAIGN_NAME = 'span[class="campaign-title__name"]'
    TEXT = 'div[class="banner-preview__middleright"] p[data-name="text"][class="banner-preview__text"]'
    TITLE = 'div[class="banner-preview__top"] span[class="banner-preview__title"]'
    IMAGE = 'div[class="banner-preview__middleleft"] span[class="banner-preview__img"]'

    @property
    def compaignName(self):
        if not hasattr(self, '__compaignNameInitDone'):
            setattr(self, '__compaignName', Text(waitAndFind2(self.element, self.COMPAIGN_NAME)))
            setattr(self, '__compaignNameInitDone', True)
        return getattr(self, '__compaignName')


    @property
    def text(self):
        if not hasattr(self, '__textInitDone'):
            setattr(self, '__text', Text(waitAndFind(self.element, self.TEXT)))
            setattr(self, '__textInitDone', True)
        return getattr(self, '__text')

    @property
    def title(self):
        if not hasattr(self, '__titleInitDone'):
            setattr(self, '__title', Text(waitAndFind(self.element, self.TITLE)))
            setattr(self, '__titleInitDone', True)
        return getattr(self, '__title')

    @property
    def image(self):
        if not hasattr(self, '__imageInitDone'):
            setattr(self, '__image', Image(waitAndFind(self.element, self.IMAGE)))
            setattr(self, '__imageInitDone', True)
        return getattr(self, '__image')
