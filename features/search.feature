Feature: Search Page

    Background:
        Given we visit Armut
        Then verify logo


    Scenario: select service
        When you select service
        Then select from popular
        Then select plus

    Scenario: search service
        When you search Temizlik
        Then you should see title