from conftest import URLS
from ui.locators.edu_vk_locators import AuthPageLocators
from ui.pages.base_page import BasePage


class LoginPage(BasePage):
    url = URLS.EDU_VK_URL
    locators = AuthPageLocators()

    def login(self, user, password):
        self.click(self.locators.AUTH_BTN)
        self.click(self.locators.SIGNUP_LINK)
        self.find(self.locators.EMAIL_INPUT).send_keys(user)
        self.find(self.locators.PASSWORD_INPUT).send_keys(password)
        self.click(self.locators.LOGIN_BTN)
        self.wait().until(
            lambda d: d.current_url != self.url and "auth" not in d.current_url
        )
