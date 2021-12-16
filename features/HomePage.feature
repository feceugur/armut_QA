Feature: Career Page

Background:
    Given we visit Armut
    Then verify logo

#Scenario: visit Armut and get a job
#    Then click on Kariyer
#    Then you found your QA Engineer

Scenario Outline: select service
    When you select <service>
    Then select from popular
    #Then select plus
  Examples:
   | service       |
   | 1             |
