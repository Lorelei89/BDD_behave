Feature: Jules sign_in tests

  Background:
     Given signin: I am a user on Jules signin page

  @signin1
  Scenario Outline: Check email error message
     When signin: I set my email "<email>"
     Then signin: I check the email error message

     Examples:
       | email    |
       | abc@.com |
       | 123@.com |

  @signin1
  Scenario: Activation error for invalidated email
    When signin: I set my email "mneculau@yahoo.com"
    When signin: I set my password "aaaa"
    When signin: I click on login button
    Then signin: I check the first login error - invalided email

  @signin
  Scenario: Activation error for invalidated email
    When signin: I set my email "mneculau@yahoo.com"
    When signin: I set my password "aaaa"
    When signin: I click on login button
    When signin: I click on send activation email button
    Then signin: I check the send activation email error message