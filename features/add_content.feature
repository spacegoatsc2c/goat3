Feature: Add Content
  I want to be able to add new content
  So that they appear on the home page

  Scenario: Add a youtube link and see it on home page

    Given I am on the home page
    When I add a youtube link "https://www.youtube.com/watch?v=7ZN-BUMErZE"
    Then I will see "https://www.youtube.com/watch?v=7ZN-BUMErZE"

  Scenario: Add multiple youtube links and see them on home page
    Given I am on the home page
    When I add a youtube link "https://www.youtube.com/watch?v=7ZN-BUMErZE"
      And I add a youtube link "https://www.youtube.com/watch?v=iXBtzGOguCc"
    Then I will see "https://www.youtube.com/watch?v=7ZN-BUMErZE"
      And I will see "https://www.youtube.com/watch?v=iXBtzGOguCc"
