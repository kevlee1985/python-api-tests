Feature: Geolocation testing
  A service which checks user's location

  Scenario: UK based IP and Coordinates
    Given Player triggers geolocation API
    Then Check the response status as 200
    And Check the response "locationOk" value as "true"
