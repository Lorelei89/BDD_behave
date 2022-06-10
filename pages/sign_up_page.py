import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SignupPage(BasePage):
    LOGIN_LINK = (By.XPATH, '//button[@data-test-id="go-to-login-btn"]')
    BUSINESS_BTN = (By.XPATH, '//input[@value="business"]')
    PERSONAL_BTN = (By.XPATH, '//input[@value="personal"]')
    CONTINUE_BTN = (By.XPATH, '//button[@data-test-id="select-account-continue-btn"]')
    FIRST_NAME_INPUT = (By.XPATH, '//input[@placeholder="Type your answer here..."]')
    LAST_NAME_INPUT = (By.XPATH, '//input[@placeholder="Type your answer here..."]')
    ENTER_EMAIL_INPUT = (By.XPATH, '//div[@class="css-13k67qp"]//input[@aria-invalid="false"]')
    SET_PASS_INPUT = (By.XPATH, '//div[@class="css-c9auvn"]//input[@aria-invalid="false"]')
    SEND_EMAIL_AGAIN_BTN = (By.XPATH, '//button[@data-test-id="resend-activation-email-btn"]')
    EMAIL_ERROR = (By.XPATH, '//p[contains(text(),"Please enter")]')
    EMPTY_INPUT_ERROR = (By.XPATH, '//p[contains(text(),"invalid")]')
    VALID_F_NAME = (By.XPATH, '//input[@value="George"]')

    def click_on_log_in_link(self):
        self.driver.find_element(*self.LOGIN_LINK).click()

    def click_on_business_btn(self):
        self.driver.find_element(*self.BUSINESS_BTN).click()

    def click_on_personal_btn(self):
        self.driver.find_element(*self.PERSONAL_BTN).click()
        time.sleep(1)

    def click_on_continue_btn(self):
        self.driver.find_element(*self.CONTINUE_BTN).click()

    def enter_first_name(self, first_name):
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)
        time.sleep(2)

    def enter_last_name(self, last_name):
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)

    def enter_email(self, enter_email):
        self.driver.find_element(*self.ENTER_EMAIL_INPUT).send_keys(enter_email)

    def set_pass(self, password):
        self.driver.find_element(*self.SET_PASS_INPUT).send_keys(password)

    def confirm_pass(self, confirm_password):
        self.driver.find_element(*self.SET_PASS_INPUT).send_keys(confirm_password)

    # methods for verification
    def verify_invalid_email_msg(self):
        error_msg = self.driver.find_element(*self.EMAIL_ERROR).text
        self.assertIn(error_msg, 'Please enter a valid email address.', 'Incorrect email error message')

    def verify_empty_input_error(self):
        error_msg = self.driver.find_element(*self.EMPTY_INPUT_ERROR).text
        self.assertIn(error_msg, 'invalid field value', 'Incorrect empty input error')

    def verify_correct_first_name(self):
        expected = self.driver.find_element(*self.FIRST_NAME_INPUT).text
        actual = ""
        self.assertEqual(expected, actual, 'There is name in first_name input')
