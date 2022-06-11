from behave import *


@when('forgot_password: I set my email "{email}"')
def set_impl(context, email):
    context.forgot_password_page.set_email(email)


@when('forgot_password: I click on back to login link')
def set_impl(context):
    context.forgot_password_page.click_on_back_to_login()


@when('forgot_password: I click on signup link')
def set_impl(context):
    context.forgot_password_page.click_on_sign_up_link()


@then('forgot_password: I verify that the email validation message is correct')
def set_impl(context):
    context.forgot_password_page.verify_email_error_msg()

