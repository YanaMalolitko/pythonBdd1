Feature: Add a pet to the store
  In order to sale a pet I would like
  to add a profile information to pet store web site
  and remove the profile when particular pet is sold

Background:
  Given All pet store credentials are defined


  Scenario Outline: Add a pet profile to the store
    When I add the pet profile information with "<id>" to the "<website>"
    And Receive status code response 200
    Then I request the pet by "<id>"
    And Receive data format is proper
    Examples:
      | website                           | id   |
      | http://petstore.swagger.io/v2/pet/ | 9876 |

  Scenario Outline: Remove a pet profile from the store
    When I remove the pet profile information with "<id>" from the "<website>"
    Then I request the pet by "<id>"
    And Receive status code response 404
    Examples:
      | website                           | id   |
      | http://petstore.swagger.io/v2/pet/ | 9876 |