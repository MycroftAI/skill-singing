Feature: mycroft-singing

  Scenario: ask mycroft to sing a song
    Given an english speaking user
    And Mycroft is not singing
      When the user says "sing a song"
      Then "mycroft-singing" should reply with dialog from "singing.dialog"
      And mycroft should sing

  Scenario: ask mycroft to stop singing
    Given an english speaking user
    And Mycroft is singing
      When the user says "stop singing"
      Then mycroft should stop singing


