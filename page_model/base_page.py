import logging
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utilities import custom_logger as cl

from traceback import print_stack
import time
import os


class BasePage:

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def get_URL(self, URL):
        '''
        :return: base URL, notice no ending slash
        '''
        self.log.info(f'Go to URL: {URL}')
        return self.driver.get(URL)


    def get_title(self):
        '''
        :return: title of a current URL
        '''
        return self.driver.title

    # def navi_links_list(self):
    #     '''
    #     returns list of navi links
    #     '''
    #     return self.driver.find_elements(*BasePageLocators._nav_links)

    def scroll_page(self, distance):
        '''
        distance: int
        Scrolls down current page by <distance> pixels.
        For scrolling up provide negative integer
        '''
        self.log.info(f'Scrolling page by {distance} px.')
        return self.driver.execute_script(f"window.scrollBy(0, {distance});")

    # def buttons_list(self):
    #     '''
    #     :return: List of buttons, elements with class name 'btn'
    #     '''
    #     return self.driver.find_elements(*BasePageLocators._buttons)

    def wait_for_element_to_click(self, locator):
        '''
        waits for element
        :param locator: tuple with no *
        '''
        WebDriverWait(self.driver, timeout=15).until(
            expected_conditions.element_to_be_clickable(locator))  # provide unpacked tuple

    def click_element(self, locatorType, locator):
        '''
        clicks on element
        as arguments you provide *tuple
        '''
        self.driver.find_element(locatorType, locator).click()
        self.log.info(f'Item with locator: {locator} clicked.')

    def is_element_displayed(self, locatorType, locator):
        '''
        Checks if element is displayed
        as arguments you provide *tuple
        '''
        self.driver.find_element(locatorType, locator).is_displayed()
        self.log.info('Verifying is element displayed.')

    def take_screenshot(self, resultMessage):
        '''
        Takes screenshot of a currently open web page
        '''

        # we create a path working on every computer
        fileName = resultMessage + '.' + str(round(time.time() * 1000)) + '.png'
        screenShotsDirectory = '../screenshots/'
        relativeFileName = screenShotsDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenShotsDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info('Screenshot saved to directory: ' + destinationFile)
        except:
            self.log.error("### Exception Occurred - taking screenshot")
        print_stack()

    # def send_keys_to_element(self, locatorType, locator, text):
    #     element = self.driver.find_element(locatorType, locator)
    #     element.send_keys(text)