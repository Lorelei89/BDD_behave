Feature: Jules forgot_password tests

  Background:
    Given signin: I am a user on Jules signin page

  @forgot_password
  Scenario: Wrong email validation message
    When signin: I click on forgot_password_link
    When forgot_password: I set my email "abc"
    Then forgot_password: I verify that the email validation message is correct

  @forgot_password
  Scenario Outline: Wrong email validation message
    When signin: I click on forgot_password_link
    When forgot_password: I set my email "<email>"
    Then forgot_password: I verify that the email validation message is correct

    Examples:
     | email      |
     | abcde@.com |
     | 12345@.com |

  @forgot_password
  Scenario: Verification of back to login functionality
    When signin: I click on forgot_password_link
    When forgot_password: I click on back to login link
    Then signin: I verify if word account exists on page

  @forgot_password
  Scenario: Verification of sign-up functionality on forgot-password page
    When signin: I click on forgot_password_link
    When forgot_password: I click on signup link
    Then signup: I verify signup word to match title on signup page
