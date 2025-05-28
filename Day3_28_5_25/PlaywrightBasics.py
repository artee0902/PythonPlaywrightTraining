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


def test_playwright_shortcut(page):       #page fixture coming from Page Class i.e. page:Page
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("lefdarning")
    page.get_by_role("combobox").select_option("Teacher")
    page.locator("#terms").check()
    page.wait_for_timeout(3000)
    page.get_by_role("link",name="terms and conditions")
    page.get_by_role("button",name="Sign In").click()
    page.wait_for_timeout(3000)
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()






