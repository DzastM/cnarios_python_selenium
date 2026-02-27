Feature: Product Purchasing

    Scenario: Add multiple products to cart and verify cart content 
        Given I am on the product purchasing page
        When I add "Wireless Headphones" to the cart
        And I add "Fitness Band" to the cart
        And I add "Laptop Backpack" to the cart
        And I view the cart
        Then the cart should contain 1 "Wireless Headphones", 1 "Fitness Band", and 1 "Laptop Backpack"
        And total price should be <total_price>

    Scenario: Increase and decrease product quantity 
        Given I am on the product purchasing page
        When I add "Wireless Headphones" to the cart
        And I add "Fitness Band" to the cart
        And I view the cart
        Then I should see 1 "Wireless Headphones" and 1 "Fitness Band"
        When I increase the quantity of "Wireless Headphones" to 5
        Then the cart should contain 5 "Wireless Headphones" and 1 "Fitness Band"
        When I increase the quantity of "Fitness Band" to 3
        And I descrease the quantity of "Wireless Headphones" to 2
        Then the cart should contain 2 "Wireless Headphones" and 3 "Fitness Band"
        And total price should be <total_price>

    Scenario: Remove products from cart and verify cart content
        Given I am on the product purchasing page
        When I add "Smartphone Stand" to the cart
        And I add "Fitness Band" to the cart
        And I add "Bluetooth Speaker" to the cart
        And I view the cart
        And I remove "Fitness Band" from the cart
        Then the cart should contain 1 "Smartphone Stand" and 1 "Bluetooth Speaker"
        And the cart should not contain "Fitness Band"
        And total price should be <total_price>

