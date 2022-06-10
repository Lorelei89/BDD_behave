from behave import *


@when('signup: I click on log in link')
def set_impl(context):
    context.sign_up_page.click_on_log_in_link()


@when('signup: I click on business button')
def set_impl(context):
    context.sign_up_page.click_on_business_btn()


@when('signup: I click on personal button')
def set_impl(context):
    context.sign_up_page.click_on_personal_btn()


@when('signup: I click on continue button')
def set_impl(context):
    context.sign_up_page.click_on_continue_btn()


@when('signup: I click on continue button after entering first name')
def set_impl(context):
    context.sign_up_page.click_on_continue_btn2()


@when('signup: I click on continue button after entering last name')
def set_impl(context):
    context.sign_up_page.click_on_continue_btn3()


@when('signup: I enter my first name "{first_name}"')
def set_impl(context, first_name):
    context.sign_up_page.enter_first_name(first_name)


@when('signup: I enter my last name "{last_name}"')
def set_impl(context, last_name):
    context.sign_up_page.enter_last_name(last_name)


@when('signup: I enter my email "{email}"')
def set_impl(context, email):
    context.sign_up_page.enter_email(email)


@then('signup: I verify the email error message')
def set_impl(context):
    context.sign_up_page.verify_invalid_email_msg()


@then('signup: I verify the error for empty input')
def set_impl(context):
    context.sign_up_page.verify_empty_input_error()


@then('signup: I verify first_name input name to match to ""')
def set_impl(context):
    context.sign_up_page.verify_correct_first_name()
