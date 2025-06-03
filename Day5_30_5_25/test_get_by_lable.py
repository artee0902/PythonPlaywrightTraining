import pytest
from playwright.sync_api import sync_playwright, Page

@pytest.fixture(scope="module")
def page():
    print("Setting up Playwright and launching browser...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(record_video_dir="videos/")
        context.tracing.start(title="Login Test Trace", screenshots=True, snapshots=True, sources=True)
        page = context.new_page()
        page.goto("https://rahulshettyacademy.com/loginpagePractise/")
        yield page
        print("Stopping tracing and closing browser...")
        context.tracing.stop(path="trace.zip")
        context.close()
        browser.close()

def test_playwright_shortcut(page: Page):
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("Teacher")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_timeout(3000)
