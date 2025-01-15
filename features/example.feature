Feature: Search on Playwright website

  Scenario: Search for Playwright
    Given I am on the Playwright homepage
    When I search for "Playwright"
    Then I should see "Getting started with Playwright" in the results
