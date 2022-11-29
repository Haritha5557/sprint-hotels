Feature: Make My Trip
  Scenario: Search Hotel
    Given I launch browser
    When I open make my trip
    When click on hotel
    And click on search and enter name
    And click on check-in
    And click on check-out
    And click on rooms & guests
    And select rooms and adults and children
    And select children age
    And click on apply
    When I click on search and navigate
    And click on hotel