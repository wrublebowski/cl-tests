from selenium.webdriver import ActionChains
import time
from locators.home_locators import HomePageLocators
from page_model.base_page import BasePage

class HomePage(BasePage):
    # create instance of Page Object Model

    def click_on_joinus(self):

        careers_link = self.driver.find_element(*HomePageLocators._careers_link)
        joinus_link = self.driver.find_element(*HomePageLocators._joinus_link)
        try:
            # create instance for ActionChains class and perform action
            action1 = ActionChains(self.driver)
            action1.move_to_element(careers_link).perform()
            time.sleep(1)
            # click by actions.method, remember about .perform()!
            action1.move_to_element(joinus_link).click().perform()
            self.log.info('Item clicked successfully with mouse hoovering!')
        except:
            self.log.info('action with Mouse Hoovering failed!')

    def click_on_people(self):

        careers_link = self.driver.find_element(*HomePageLocators._careers_link)
        people_link = self.driver.find_element(*HomePageLocators._people_at_cl)
        try:
            # create instance for ActionChains class and perform action
            action1 = ActionChains(self.driver)
            action1.move_to_element(careers_link).perform()
            time.sleep(1)
            # click by actions.method, remember about .perform()!
            action1.move_to_element(people_link).click().perform()
            self.log.info('Item clicked successfully with mouse hoovering!')
        except:
            self.log.info('action with Mouse Hoovering failed!')

    def click_on_search(self):
        self.click_element(*HomePageLocators._search_tool)

    # def enter_kubernetes(self):
    #     self.send_keys_to_element(*HomePageLocators._search_box, 'kubernetes')