from conftest import URLS
from ui.locators.edu_vk_locators import SchedulePageLocators
from ui.pages.base_page import BasePage
from enum import Enum


class ScheduleInterval(Enum):
    NEAR = "near"
    SEMESTER = "semester"


class WrongIntervalException(Exception):
    pass


class SchedulePage(BasePage):
    url = URLS.SCHEDULE_URL
    locators = SchedulePageLocators()

    def select_interval(self, interval):
        self.click(self.locators.SCHEDULE_INTERVAL(interval))

    def select_subject(self, subject):
        self.click(self.locators.SUBJ_SELECTOR)
        self.click(self.locators.SUBJ_SELECTOR_ELEM(subject))

    def get_subjects(self):
        elems = self.driver.find_elements(*self.locators.SUBJS)
        self.wait().until(lambda x: "loading" not in x.find_element(*self.locators.SCHEDULE).get_attribute('class'))
        self.wait().until(lambda x: x.find_elements(*self.locators.SUBJS) != elems)

        subjs = {}
        elems = self.driver.find_elements(*self.locators.SUBJS)
        for elem in elems:
            name = elem.find_element(*self.locators.SUBJ_NAME).text.strip()
            date = elem.find_element(*self.locators.SUBJ_DATE).text.strip()
            subjs[name] = date
        return subjs
            