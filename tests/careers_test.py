import unittest
from page_model.home_page import HomePage
from page_model.careers_page import CareersPage
import pytest

@pytest.mark.usefixtures('one_time_set_up', 'set_up')
class TestCareer(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_set_up(self, one_time_set_up):
        self.hp = HomePage(self.driver)
        self.cp = CareersPage(self.driver)
        print('----------fixture: inside class test')

    def test1_job_for_me(self):
        self.hp.click_on_joinus()
        self.cp.look_for_job()
        assert self.cp.verify_job_req() == True

    def test2_crew_page(self):
        self.hp.click_on_people()
        expected_title = 'work and have fun'
        print(f"Verifying if '{expected_title}' matches '{self.cp.get_title()}'")
        assert expected_title in self.cp.get_title().lower()