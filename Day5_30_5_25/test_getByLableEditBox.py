import pytest
import re
from playwright.sync_api import sync_playwright, expect


@pytest.fixture(scope="module")
def page():
    print("Setting up Playwright and launching browser...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://rahulshettyacademy.com/loginpagePractise/")
        yield page
        print("Closing browser...")
        browser.close()


@pytest.fixture(scope="function")
def login_fixture(page):
    # Fill in login form using IDs (not labels)
    page.locator("#username").fill("rahulshettyacademy")
    page.locator("#password").fill("learning")
    page.get_by_role("combobox").select_option("Teacher")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()

    # Wait until redirected to the shop page
    page.wait_for_url(re.compile(".*shop"))


def test_add_to_cart(page, login_fixture):
    # Ensure product cards are loaded
    page.wait_for_selector("app-card")

    # Click "Add" on specific products
    page.locator("app-card").filter(has_text="iphone X").locator("button").click()
    page.locator("app-card").filter(has_text="Nokia Edge").locator("button").click()

    # Proceed to checkout
    page.get_by_text("Checkout").click()

    # Wait until cart items are visible
    page.wait_for_selector(".media-body")

    # Assert 2 items in cart
    expect(page.locator(".media-body")).to_have_count(2)
