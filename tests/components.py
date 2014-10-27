
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions
#from selenium.webdriver.common.keys import Keys
#from datetime import datetime
#from tests.page_objects.Const import Const


from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from tests.atoms import Element, ImageGrabber, Image, Button, Text, Textbox, Radiobutton, Groupbox, Checkbox

DEBUG = True

class Component(object):
    def __init__(self, driver):
        self.driver = driver



def waitAndFind2(driver, targetName):
    debug ("looking for " + targetName)
    result =  WebDriverWait(driver, 30, 0.1).until(
       lambda d: d.find_elements_by_css_selector(targetName)
    )
    debug ("found " + str(len(result)))

    result =  WebDriverWait(driver, 10, 0.5).until(
        lambda d: d.find_element_by_css_selector(targetName)
    )
    return result

def waitAndFind(driver, targetName):
    result =  WebDriverWait(driver, 10, 0.5).until(
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

def createOnFirstAccess(self, name, constructor, selector, searchMetod = waitAndFind2):
    debug ("createOnFirstAccess " + name)
    initName = '__' + name + 'InitDone'
    objectName = '__' + name
    invalidateName = 'invalidate'
    checkName = 'check'
    if not hasattr(self, initName) or getattr(self, initName) == False:
        debug ("create " + name)
        setattr(self, objectName, constructor(searchMetod(self.element, selector)))
        setattr(self, initName, True)
    if not hasattr(self, invalidateName):
        debug ("set invalidate ")
        setattr(self, invalidateName, invalidateFunction)
    return getattr(self, objectName)

def invalidateFunction(parent, name):
    debug ("invalidateFunction " + name)
    initName = '__' + name + 'InitDone'
    if hasattr(parent, initName):
        if getattr(parent, initName) == True:
            debug ("invalidate " + name)
            setattr(parent, initName, False)
        else:
            debug ("already invalidated " + name)
    else:
        debug ("no attribute " + name)
    pass

def debug(text):
    if DEBUG:
        print text

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
    IMAGE_PREVIEW = 'div[class="js-image-img"] span[class="banner-preview__img"]'


    @property
    def title(self):
        return createOnFirstAccess(self, "title", Textbox, self.TITLE)

    @property
    def text(self):
        return createOnFirstAccess(self, "text", Textbox, self.TEXT)

    @property
    def link(self):
        return createOnFirstAccess(self, "link", Textbox, self.LINK)

    @property
    def submit(self):
        return createOnFirstAccess(self, "submit", Button, self.SUBMIT)

    @property
    def imageGrabber(self):
        return createOnFirstAccess(self, "imageGrabber", ImageGrabber, self.IMAGE_GRABBER)

    @property
    def image(self):
        return createOnFirstAccess(self, "image", Image, self.IMAGE_PREVIEW)

class Income(Element):
    LOW = 'input[id="income_group-9286"]'
    MEDIUM = 'input[id="income_group-9287"]'
    HIGH = 'input[id="income_group-9288"]'
    LOCK = 'div[data-name="income_group"] span[class*="campaign-setting__value"]'

    @property
    def lock(self):
        return createOnFirstAccess(self, "lock", Groupbox, self.LOCK)

    @property
    def low(self):
        return createOnFirstAccess(self, "low", Checkbox, self.LOW)

    @property
    def medium(self):
        return createOnFirstAccess(self, "medium", Checkbox, self.MEDIUM)

    @property
    def high(self):
        return createOnFirstAccess(self, "high", Checkbox, self.HIGH)

class WhomBlock(Element):

    INCOME_GROUP = 'li[data-name="income_group"]'

    @property
    def income(self):
        return createOnFirstAccess(self, "income", Income, self.INCOME_GROUP)

class BannerPreview(Element):
    TITLE = 'span[class="banner-preview__title"]'
    TEXT = 'p[class="banner-preview__text"]'
    IMAGE = 'div[class="js-image-img"] span[class="banner-preview__img"]'
    #IMAGE = 'span[class="banner-preview__img"]'

    @property
    def title(self):
        return createOnFirstAccess(self, "title", Text, self.TITLE)

    @property
    def text(self):
        return createOnFirstAccess(self, "text", Text, self.TEXT)

    @property
    def image(self):
        return createOnFirstAccess(self, "image", Image, self.IMAGE)

class WhenBlock(Element):
    TIME = 'li[data-name="fulltime"]'

    @property
    def timeBlock(self):
        return createOnFirstAccess(self, "timeBlock", TimeBlock, self.TIME)

class TimeBlock(Element):
    BUTTON_WORKTIME = 'li[data-name="workTime"]'
    LOCK = 'div[data-name="fulltime"] span[class*="campaign-setting__value"]'
    CHECKBOX_MONDAY_0 = 'ul[data-name="mon"] li[data-id="0"]'

    @property
    def workTime(self):
        return createOnFirstAccess(self, "workTime", Button, self.BUTTON_WORKTIME)

    @property
    def monday0(self):
        return createOnFirstAccess(self, "monday0", Groupbox, self.CHECKBOX_MONDAY_0)

    @property
    def lock(self):
        return createOnFirstAccess(self, "lock", Groupbox, self.LOCK)

    @property
    def text(self):
        return createOnFirstAccess(self, "text", Text, self.LOCK)


class FooterBlock(Element):
    BUTTON = 'span[class="main-button__label"]'

    @property
    def submit(self):
        return createOnFirstAccess(self, "submit", Button, self.BUTTON)
#////////////////////////////////////////////////////////////////////////////////////////////////////////////

class CompaignsList(Element):
    LAST_COMPAIGN = 'li[class="campaign-row"]'

    @property
    def compaign(self):
        return createOnFirstAccess(self, "compaign", Compaign, self.LAST_COMPAIGN)

class Compaign(Element):
    COMPAIGN_NAME = 'span[class="campaign-title__name"]'
    TEXT = 'div[class="banner-preview__middleright"] p[data-name="text"][class="banner-preview__text"]'
    TITLE = 'div[class="banner-preview__top"] span[class="banner-preview__title"]'
    IMAGE = 'div[class="banner-preview__middleleft"] span[class="banner-preview__img"]'

    @property
    def compaignName(self):
        return createOnFirstAccess(self, "compaignName", Text, self.COMPAIGN_NAME)


    @property
    def text(self):
        return createOnFirstAccess(self, "text", Text, self.TEXT, waitAndFind)

    @property
    def title(self):
        return createOnFirstAccess(self, "title", Text, self.TITLE, waitAndFind)

    @property
    def image(self):
        return createOnFirstAccess(self, "image", Image, self.IMAGE, waitAndFind)
