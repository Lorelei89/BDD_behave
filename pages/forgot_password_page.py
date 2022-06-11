from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ForgotPassword(BasePage):
    EMAIL_INPUT = (By.XPATH, '//*[@placeholder="Enter your email"]')
    SEND_EMAIL_BTN = (By.XPATH, '//*[@class="css-17qmje5"]//parent::button')
    EMAIL_ERROR = (By.XPATH, '//p[contains(text(), "email")]')
    BACK_TO_LOGIN = (By.XPATH, '//a[@data-test-id="sign-in-link"]')
    SIGN_UP_BTN = (By.XPATH, '//a[@data-test-id="sign-up-link"]')

    def set_email(self, email):
        self.wait_for_elem(*self.EMAIL_INPUT)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        sleep(1)

    def click_send_email_btn(self):
        self.driver.find_element(*self.SEND_EMAIL_BTN).click()

    def click_on_back_to_login(self):
        self.driver.find_element(*self.BACK_TO_LOGIN).click()

    def click_on_sign_up_link(self):
        self.driver.find_element(*self.SIGN_UP_BTN).click()

    def verify_email_error_msg(self):
        expected = 'Please enter a valid email address!'
        actual = self.driver.find_element(*self.EMAIL_ERROR).text
        self.assertEqual(expected, actual, 'The email error message not correct')
