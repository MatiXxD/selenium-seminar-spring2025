from selenium.webdriver.common.by import By

class AuthPageLocators:
    AUTH_BTN_LOCATOR = (By.CLASS_NAME, "gtm-auth-header-btn")
    SIGNUP_LINK_LOCATOR = (By.CLASS_NAME, "gtm-signup-modal-link")
    LOGIN_BTN_LOCATOR = (By.CLASS_NAME, "gtm-login-btn")
    EMAIL_INPUT_LOCATOR = (By.ID, "email")
    PASSWORD_INPUT_LOCATOR = (By.ID, "password")
    
class SearchPeoplePageLocators:
    SEARCH_INPT_LOCATOR = (By.XPATH, "//input[@name='q' and @class='input-text']")
    SEARCH_BTN_LOCATOR = (By.XPATH, "//input[@type='submit' and @class='input-submit']")
    SEARCH_PEOPLE_LOCATOR = (By.CSS_SELECTOR, "td.cell-name")
    SEARCH_PEOPLE_NAME_LOCATOR = (By.CSS_SELECTOR, "p.realname")
    SEARCH_PEOPLE_GROUP_LOCATOR = (By.CSS_SELECTOR, "span.user-group")

class SchedulePageLocators:
    SUBJ_SELECTOR_LOCATOR = (By.CSS_SELECTOR, ".r-input-select")
    SUBJ_SELECTOR_ELEM_LOCATOR = staticmethod(lambda subj: (By.XPATH, f"//*[contains(text(), '{subj}')]"))
    SCHEDULE_INTERVAL_LOCATOR = staticmethod(lambda interval: (By.XPATH, f"//*[@intervalid='{interval}']"))
    SCHEDULE_LOCATOR = (By.CSS_SELECTOR, "table.schedule-timetable")
    SUBJS_LOCATOR = (By.CSS_SELECTOR, "tr.lessonItem")
    SUBJ_NAME_LOCATOR = (By.XPATH, './/td[contains(@class, "item__event")]//a/strong')
    SUBJ_DATE_LOCATOR = (By.XPATH, './/td[contains(@class, "item__date")]//strong')
