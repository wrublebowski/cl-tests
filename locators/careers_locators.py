from selenium.webdriver.common.by import By

class CareersPageLocators():

    _open_positions_link = By.XPATH, '// a[contains(text(), "See open positions")]'
    _quality_a_e_intern = By.XPATH, "//div[@id='job_offers_results']//figcaption[contains(text(),'Quality Assurance')]"
    _selenium_req = By.XPATH, "//li[contains(text(),'Selenium')]"
    _accept_cookie = By.ID, "cn-accept-cookie"