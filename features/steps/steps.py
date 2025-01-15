from playwright.sync_api import sync_playwright
from behave import given, when, then

@given("I am on the Playwright homepage")
def step_open_homepage(context):
    with sync_playwright() as p:
        context.browser = p.chromium.launch(headless=False)
        context.page = context.browser.new_page()
        context.page.goto("https://playwright.dev/")

@when('I search for "{query}"')
def step_search(context, query):
    context.page.fill('input[type="search"]', query)
    context.page.press('input[type="search"]', 'Enter')

@then('I should see "{expected_text}" in the results')
def step_verify_results(context, expected_text):
    assert expected_text in context.page.text_content('body')
    context.browser.close()
