from behave import *


@given('signin: I am a user on Jules signin page')
def step_impl(context):
    context.sign_in_page.navigate_to_sign_in_page()


@when('signin: I set my email "{email}"')
def set_impl(context, email):
    context.sign_in_page.set_email(email)


@when('signin: I set my password "{pswd}"')
def set_impl(context, pswd):
    context.sign_in_page.set_pass(pswd)


@when('signin: I click on login button')
def set_impl(context):
    context.sign_in_page.click_login_btn()


@when('signin: I click on forgot_password_link')
def set_impl(context):
    context.sign_in_page.click_forgot_pass_link()
