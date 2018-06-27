Feature: Add Content
  I want to be able to add new content
  So that they appear on the home page

  Scenario: Add a youtube link and see it on home page

    Given I am on the home page
    When I add a youtube link "https://www.youtube.com/watch?v=7ZN-BUMErZE"
    Then I will see a link to "https://www.youtube.com/watch?v=7ZN-BUMErZE" on the home page
