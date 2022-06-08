Feature: Jules forgot_password tests

  Background:
    Given signin: I am a user on Jules signin page

  @jules
  Scenario: Wrong email validation message
    When signin: I click on forgot_password_link
    When forgot_password: I set my email "abc"
    Then forgot_password: I verify that the email validation message is correct

  @jules
  Scenario Outline: Wrong email validation message
    When signin: I click on forgot_password_link
    When forgot_password: I set my email "<email>"
    Then forgot_password: I verify that the email validation message is correct

    Examples:
     | email      |
     | abcde@.com |
     | 12345@.com |
