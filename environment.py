from browser import Browser
from pages.forgot_password_page import ForgotPassword
from pages.sign_up_page import SignupPage
from pages.sing_in_page import SigninPage


def before_all(context):
    context.browser = Browser()  # object
    context.sign_in_page = SigninPage()
    context.forgot_password_page = ForgotPassword()
    context.sign_up_page = SignupPage()


def after_all(context):
    context.browser.close()
