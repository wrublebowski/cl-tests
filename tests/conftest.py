import pytest
from selenium import webdriver

@pytest.fixture()
def set_up():
    print('------fixture before method')
    yield
    print('------fixture after method')

@pytest.fixture(scope='class')
def one_time_set_up(request):
    print('------fixture before class')
    baseURL = "https://codilime.com/"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(4)
    driver.get(baseURL)

    # to pass forward driver must have:
    request.cls.driver = driver
    yield driver
    print('------fixture after class')
    driver.quit()