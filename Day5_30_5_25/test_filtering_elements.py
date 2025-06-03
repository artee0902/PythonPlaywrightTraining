import pytest
from playwright.sync_api import sync_playwright, expect
import re

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
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("Teacher")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_url(re.compile(".*shop"))  # More reliable than fixed timeout

def test_add_to_cart(page, login_fixture):
    page.wait_for_selector("app-card")  # Wait for product cards to appear

    # Debug: print all product card titles
    cards = page.locator("app-card")
    print(f"Cards count: {cards.count()}")
    for i in range(cards.count()):
        print(cards.nth(i).inner_text())

    # Attempt to add items to cart
    page.locator("app-card").filter(has_text="iphone X").locator("button").click()
    page.locator("app-card").filter(has_text="Nokia Edge").locator("button").click()

    page.get_by_text("Checkout").click()
    page.wait_for_selector(".media-body")

    expect(page.locator(".media-body")).to_have_count(2)
