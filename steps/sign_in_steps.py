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


@when('signin: I click on sign_up link')
def set_impl(context):
    context.sign_in_page.click_on_sign_up_link()


@when('signin: I click on send activation email button')
def set_impl(context):
    context.sign_in_page.click_on_activ_err2_btn()


@then('signin: I verify if word account exists on page')
def set_impl(context):
    context.sign_in_page.verify_correct_text_in_page()


@then('signin: I check the email error message')
def set_impl(context):
    context.sign_in_page.check_email_error_msg()


# @then('signin: I check the password error message')
# def set_impl(context):
#     context.sign_in_page.check_pass_error_msg()

@then('signin: I check the first login error - invalided email')
def set_impl(context):
    context.sign_in_page.check_err1_invalided_email()


@then('signin: I check the send activation email error message')
def set_impl(context):
    context.sign_in_page.check_err1_invalided_email()
