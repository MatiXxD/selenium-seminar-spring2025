import os
import pytest

from selenium.webdriver.remote.webdriver import WebDriver
from _pytest.fixtures import FixtureRequest
from dotenv import load_dotenv
from conftest import URLS

from ui.pages.login_page import LoginPage
from ui.pages.search_page import SearchPeoplePage
from ui.pages.schedule_page import SchedulePage

class BaseCase:
    driver: WebDriver

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config
        request.addfinalizer(self.driver.delete_all_cookies)


@pytest.fixture(scope="session")
def credentials():
    load_dotenv()
    return {"login": os.getenv("LOGIN"), "password": os.getenv("PASSWORD")}


@pytest.fixture(scope="session")
def cookies(credentials, driver):
    login_page = LoginPage(driver)
    login_page.login(credentials["login"], credentials["password"])
    return driver.get_cookies()


class TestLogin(BaseCase):
    @pytest.fixture(autouse=True)
    def setup_test(self, driver):
        self.login_page = LoginPage(driver)

    def test_login_page(self, credentials):
        self.login_page.login(credentials["login"], credentials["password"])
        assert self.driver.current_url == URLS.FEED_URL


class TestLK(BaseCase):
    PEOPLE_QUERY = "Быстров"
    PEOPLE_SEARCH_TARGET_NAME = "Даниил Быстров"
    PEOPLE_SEARCH_TARGET_GROUP = "Студент"
    
    SCHEDULE_SUBJ_NAME = "End-to-End тесты на Python"
    SCHEDULE_SUBJ_DATE = "3 апреля 2025"
    
    @pytest.fixture(autouse=True)
    def setup_cookies(self, cookies):
        for cookie in cookies:
            self.driver.add_cookie(cookie)
    
    @pytest.fixture()
    def setup_people_search(self, driver):
        self.search_people_page = SearchPeoplePage(driver)
    
    @pytest.fixture()
    def setup_schedule(self, driver):
        self.schedule_page = SchedulePage(driver)

    def test_find_people(self, request):
        request.getfixturevalue("setup_people_search")
        found = self.search_people_page.find_people(self.PEOPLE_QUERY)
        assert((self.PEOPLE_SEARCH_TARGET_NAME, self.PEOPLE_SEARCH_TARGET_GROUP) in found)

    def test_schedule(self, request):
        request.getfixturevalue("setup_schedule")
        self.schedule_page.select_interval("semester")
        self.schedule_page.select_subject("Обеспечение качества в разработке ПО")
        schedule = self.schedule_page.get_subjects()
        assert self.SCHEDULE_SUBJ_NAME in schedule.keys()
        assert schedule[self.SCHEDULE_SUBJ_NAME] == self.SCHEDULE_SUBJ_DATE
