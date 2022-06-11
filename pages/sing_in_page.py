from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SigninPage(BasePage):
    EMAIL_INPUT = (By.XPATH, '//*[@placeholder="Enter your email"]')
    PASS_INPUT = (By.XPATH, '//*[@placeholder="Enter your password"]')
    LOGIN_BTN = (By.XPATH, '//*[@class="css-17qmje5"]//parent::button')
    FORGOT_PASS_LINK = (By.XPATH, '//*[@data-test-id="forgot-password-link"]')
    SIGN_UP_LINK = (By.XPATH, '//a[@class="jss17 jss19"]')
    ACCOUNT_TXT = (By.XPATH, '//span[contains(text(),"account")]')
    EMAIL_ERR_ADRS = (By.XPATH, '//*[contains(text(), "enter a valid email")]')
    PASS_ERR = (By.XPATH, '//*[contains(text(),"enter your password")]')
    LOGIN_ACTIV_ERR1 = (By.XPATH, '//div[@class="css-kknodv"]//parent::span')
    LOGIN_ACTIV_ERR2_BTN = (By.XPATH, '//div[@class="css-kknodv"]//parent::button')

    def navigate_to_sign_in_page(self):
        self.driver.get('https://jules.app/sign-in')

    def set_email(self, email):
        self.wait_for_elem(*self.EMAIL_INPUT)
        self.driver.find_element(*self.EMAIL_INPUT).click()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        sleep(1)

    def set_pass(self, pswd):
        self.driver.find_element(*self.PASS_INPUT).click()
        self.driver.find_element(*self.PASS_INPUT).send_keys(pswd)

    def click_login_btn(self):
        self.driver.find_element(*self.LOGIN_BTN).click()

    def user_login(self, email, pswd):
        self.set_email(email)
        self.set_pass(pswd)
        self.click_login_btn()

    def click_forgot_pass_link(self):
        self.driver.find_element(*self.FORGOT_PASS_LINK).click()

    def click_on_sign_up_link(self):
        self.driver.find_element(*self.SIGN_UP_LINK).click()

    def click_on_activ_err2_btn(self):
        self.driver.find_element(*self.LOGIN_ACTIV_ERR2_BTN).click()

    # methods to check
    def verify_correct_text_in_page(self):
        account_txt = self.driver.find_element(*self.ACCOUNT_TXT)
        self.assertIn(account_txt.text, f"Don't have an account?", 'Incorrect displayed text')

    def check_email_error_msg(self):
        error_msg = self.driver.find_element(*self.EMAIL_ERR_ADRS)
        self.assertIn(error_msg.text, 'Please enter a valid email address!', 'Not the correct email error')

    # def check_pass_error_msg(self):
    #     error_msg = self.driver.find_element(*self.PASS_ERR)
    #     self.assertIn(error_msg.text, 'Please enter your password!', 'Not the correct password error')

    def check_err1_invalided_email(self):
        error_msg = self.driver.find_element(*self.LOGIN_ACTIV_ERR1)
        self.assertIn(error_msg.text, 'User email is not validated.', 'Not the correct login error1')

    def check_err2_login_send_activation_email(self):
        error_msg = self.driver.find_element(*self.LOGIN_ACTIV_ERR2_BTN)
        self.assertIn(error_msg.text, 'Send activation email again', 'Send activation email again button not working')
