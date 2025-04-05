import urllib.parse

from conftest import URLS
from ui.locators.edu_vk_locators import SearchPeoplePageLocators
from ui.pages.base_page import BasePage


class SearchPeoplePage(BasePage):
    url = URLS.PEOPLE_URL
    locators = SearchPeoplePageLocators()

    def find_people(self, user):
        self.find(self.locators.SEARCH_INPT).send_keys(user)
        self.click(self.locators.SEARCH_BTN)
        
        self.wait().until(lambda d: d.current_url == f'{self.url}?{urllib.parse.urlencode({"q": user})}')
        people = self.driver.find_elements(*self.locators.SEARCH_PEOPLE)
        found = []
        for u in people:
            found.append(
                (
                    u.find_element(*self.locators.SEARCH_PEOPLE_NAME).text.strip(),
                    u.find_element(*self.locators.SEARCH_PEOPLE_GROUP).text.strip(),
                )
            )
        
        return found
