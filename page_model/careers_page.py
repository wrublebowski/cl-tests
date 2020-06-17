import time
from locators.careers_locators import CareersPageLocators
from page_model.base_page import BasePage


class CareersPage(BasePage):

    def accept_cookie(self):
        self.click_element(*CareersPageLocators._accept_cookie)

    def click_open_positions(self):
        self.click_element(*CareersPageLocators._open_positions_link)

    def click_job1(self):
        self.click_element(*CareersPageLocators._quality_a_e_intern)

    def verify_job_req(self):
        x = self.driver.find_element(*CareersPageLocators._selenium_req)
        return x.is_displayed()

    def look_for_job(self):
        self.accept_cookie()
        self.click_open_positions()
        time.sleep(2)
        self.click_job1()
        self.scroll_page(600)
        time.sleep(2)
        self.verify_job_req()