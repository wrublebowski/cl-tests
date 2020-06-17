from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
# from acceptance_tests.locators.base_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_URL(self, URL):
        '''
        :return: base URL, notice no ending slash
        '''
        print(f'Go to URL: {URL}')
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
        print(f'Scrolling page by {distance} px.')
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
        print(f'item with locator: {locator} clicked.')

    def is_element_displayed(self, locatorType, locator):
        '''
        Checks if element is displayed
        as arguments you provide *tuple
        '''
        self.driver.find_element(locatorType, locator).is_displayed()
        print('Verifying is element displayed.')

    # def send_keys_to_element(self, locatorType, locator, text):
    #     element = self.driver.find_element(locatorType, locator)
    #     element.send_keys(text)