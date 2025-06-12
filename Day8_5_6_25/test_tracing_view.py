import time
import pytest
from playwright.sync_api import sync_playwright, BrowserContext, Page, expect

@pytest.fixture(scope="module")
def setup():
    print("Setting up Playwright and launching browser...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://rahulshettyacademy.com/loginpagePractise/")
        yield context, page  # Return both context and page
        print("Closing browser...")
        browser.close()

def test_playwright_shortcut(setup):
    context, page = setup

    # Start tracing with screenshots and DOM snapshots
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("lefdarning")
    page.get_by_role("combobox").select_option("Teacher")
    page.locator("#terms").check()
    page.wait_for_timeout(3000)
    page.get_by_role("link", name="terms and conditions")
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_timeout(3000)
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    context.tracing.stop(path="trace.zip")

