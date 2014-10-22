
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

class Element(object):
    def __init__(self, element):
        self.element = element

class ImageGrabber(Element):

    def setImage(self, image):
        self.element.send_keys(image)

class Image(Element):

    def getImageUrl(self):
        result = self.element.value_of_css_property('background-image')
        return result

    def waitForPicture(self):
        result =  WebDriverWait(self.element, 10, 0.5).until(
            lambda d: self.getImageUrl() is not None
        )
        

class Button(Element):

    def click(self):
        self.element.click()
        pass

class Text(Element):

    def getText(self):
        return self.element.text


class Textbox(Element):

    def setText(self, text):
        self.element.clear()
        self.element.send_keys(text)
        pass

    def addText(self, text):
        self.element.send_keys(text)
        pass

    def getText(self):
        return self.element.getAttribute("value")

class Radiobutton(Element):
    stateChecked = False

    def setChecked(self):
        self.checkChecked()
        if not self.stateChecked:
            self.element.click()
        pass

    def checkChecked(self):
        self.stateChecked = self.element.is_selected()
        pass

    def getChecked(self):
        self.checkState()
        return stateChecked

class Groupbox(Element):
    stateOpen = False

    def open(self):
        if not self.stateOpen:
            self.element.click()
            self.stateOpen = True
        pass

    def close(self):
        if self.stateOpen:
            self.element.click()
            self.stateOpen = False
        pass

    def getState(self):
        return self.stateOpen

class Checkbox(Element):
    stateChecked = False

    def checkState(self):
        self.stateChecked = self.element.is_selected()
        pass

    def getChecked(self):
        self.checkState()
        return self.stateChecked

    def setChecked(self):
        self.checkState()
        if not self.stateChecked:
            self.element.click()
        pass

    def setUnchecked(self):
        self.checkState()
        if self.stateChecked:
            self.element.click()
        pass
