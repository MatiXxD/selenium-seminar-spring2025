from selenium.webdriver.common.by import By

class AuthPageLocators:
    AUTH_BTN = (By.CLASS_NAME, "gtm-auth-header-btn")
    SIGNUP_LINK = (By.CLASS_NAME, "gtm-signup-modal-link")
    LOGIN_BTN = (By.CLASS_NAME, "gtm-login-btn")
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    
class SearchPeoplePageLocators:
    SEARCH_INPT = (By.XPATH, "//input[@name='q' and @class='input-text']")
    SEARCH_BTN = (By.XPATH, "//input[@type='submit' and @class='input-submit']")
    SEARCH_PEOPLE = (By.CSS_SELECTOR, "td.cell-name")
    SEARCH_PEOPLE_NAME = (By.CSS_SELECTOR, "p.realname")
    SEARCH_PEOPLE_GROUP = (By.CSS_SELECTOR, "span.user-group")

class SchedulePageLocators:
    SUBJ_SELECTOR = (By.CSS_SELECTOR, ".r-input-select")
    SUBJ_SELECTOR_ELEM = staticmethod(lambda subj: (By.XPATH, f"//*[contains(text(), '{subj}')]"))
    SCHEDULE_INTERVAL = staticmethod(lambda interval: (By.XPATH, f"//*[@intervalid='{interval}']"))
    SCHEDULE = (By.CSS_SELECTOR, "table.schedule-timetable")
    SUBJS = (By.CSS_SELECTOR, "tr.lessonItem")
    SUBJ_NAME = (By.XPATH, './/td[contains(@class, "item__event")]//a/strong')
    SUBJ_DATE = (By.XPATH, './/td[contains(@class, "item__date")]//strong')
