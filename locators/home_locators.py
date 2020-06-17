from selenium.webdriver.common.by import By

class HomePageLocators():
    # locators in tuples
    _careers_link = By.ID, "menu-item-51"
    _joinus_link = By.ID, "menu-item-39"
    _people_at_cl = By.ID, "menu-item-41"
    _search_tool = By.XPATH, "//div[@class='button search_button']"
    _search_box = By.NAME, "search_keyword"