from behave import given, when, then
from pages.challenges_page import ChallengesPage
from pages.start_page import StartPage

@given("I am on the product purchasing page")
def step_given_on_product_purchasing_page(context):
    context.start_page = StartPage(context.driver)
    context.start_page.click_button("Challenges")
    context.challenges_page = ChallengesPage(context.driver)
    context.challenges_page.assert_heading("Automation Challenges")
