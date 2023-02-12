@Android
Feature: Upload Appium challenge photo via appium to android and send to email as attachment.

  Scenario: Send email attaching photo from Google photos
    Given the google photos app is launched
    When I upload photo to the app
    Then I verify the photo is uploaded
    When I tap the photo in the app
    Then I verify the image name
    When I launch the Gmail app
    And I signin into gmail account
    Then I send email attaching the photo uploaded earlier
