Feature: Jules sign_up tests

  Background:
    Given signin: I am a user on Jules signin page

  @signup1
  Scenario: Functionality of Log in link
    When signin: I click on sign_up link
    When signup: I click on log in link
    Then signin: I verify if word account exists on page

  @signup
  Scenario: Wrong email verification with 'personal' radio button
    When signin: I click on sign_up link
    When signup: I click on personal button
    When signup: I click on continue button
    When signup: I enter my first name "George"
    Then signup: I verify the error for empty input




