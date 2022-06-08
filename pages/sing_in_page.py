from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SigninPage(BasePage):
    EMAIL_INPUT = (By.XPATH, '/*[@placeholder="Enter your email"]')
    PASS_INPUT = (By.XPATH, '//*[@placeholder="Enter your password"]')
    LOGIN_BTN = (By.XPATH, '//*[@class="css-17qmje5"]//parent::button')
    FORGOT_PASS_LINK = (By.XPATH, '//*[@data-test-id="forgot-password-link"]')

    def navigate_to_sign_in_page(self):
        self.driver.get('https://jules.app/sign-in')

    def set_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def set_pass(self, pswd):
        self.driver.find_element(*self.PASS_INPUT).send_keys(pswd)

    def click_login_btn(self):
        self.driver.find_element(*self.LOGIN_BTN).click()

    def user_login(self, email, pswd):
        self.set_email(email)
        self.set_pass(pswd)
        self.click_login_btn()

    def click_forgot_pass_link(self):
        self.driver.find_element(*self.FORGOT_PASS_LINK).click()
