from conftest import URLS
from ui.locators.edu_vk_locators import SchedulePageLocators
from ui.pages.base_page import BasePage


class WrongIntervalException(Exception):
    pass


class SchedulePage(BasePage):
    url = URLS.SCHEDULE_URL
    locators = SchedulePageLocators()

    def select_interval(self, interval):
        self.click(self.locators.SCHEDULE_INTERVAL_LOCATOR(interval))

    def select_subject(self, subject):
        self.click(self.locators.SUBJ_SELECTOR_LOCATOR)
        self.click(self.locators.SUBJ_SELECTOR_ELEM_LOCATOR(subject))

    def get_subjects(self):
        elems = self.driver.find_elements(*self.locators.SUBJS_LOCATOR)
        self.wait().until(lambda x: "loading" not in x.find_element(*self.locators.SCHEDULE_LOCATOR).get_attribute('class'))
        self.wait().until(lambda x: x.find_elements(*self.locators.SUBJS_LOCATOR) != elems)

        subjs = {}
        elems = self.driver.find_elements(*self.locators.SUBJS_LOCATOR)
        for elem in elems:
            name = elem.find_element(*self.locators.SUBJ_NAME_LOCATOR).text.strip()
            date = elem.find_element(*self.locators.SUBJ_DATE_LOCATOR).text.strip()
            subjs[name] = date
        return subjs
            