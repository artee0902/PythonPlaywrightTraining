import time
import pytest
from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

@pytest.fixture(scope="module")
def page():
    print("Setting up Playwright and launching browser...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Change to True for headless
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://rahulshettyacademy.com/loginpagePractise/")
        yield page  # Provide the page to tests
        print("Closing browser...")
        browser.close()

def test_hidden_element(page):
    # Ensure the error message is hidden before interaction
    expect(page.locator(".alert-danger")).to_be_hidden()

    # Attempt to login with incorrect credentials to make the alert appear
    page.fill("#username", "wronguser")
    page.fill("#password", "wrongpass")
    page.click("#signInBtn")

    # Now the error message should be visible
    expect(page.locator(".alert-danger")).to_be_visible()
