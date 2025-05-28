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

@pytest.fixture(scope="function")
def test_playwright_shortcut(page):       #page fixture coming from Page Class i.e. page:Page
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("Teacher")
    page.locator("#terms").check()
    page.get_by_role("button",name="Sign In").click()
    page.wait_for_timeout(3000)



def test_add_to_cart(page,test_playwright_shortcut):
    iphone_product=page.locator("app-card").filter(has_text="iphone X")
    iphone_product.get_by_role("button").click()
    page.wait_for_timeout(3000)
    Nokia_product = page.locator("app-card").filter(has_text="Nokia Edge")
    Nokia_product.get_by_role("button").click()
    page.wait_for_timeout(3000)
    page.get_by_text("Checkout").click()
    time.sleep(2)
    expect(page.locator(".media-body")).to_have_count(2)


def test_child_window_handle(page,test_playwright_shortcut):
    with page.expect_popup() as newPage_info:
        page.locator(".blinkingText").click()
        time.sleep(3)
        childPage=newPage_info.value
        text=page.locator(".red").text_content()
        print(text)
        words=text.split("at")
        email=words[1].strip().split(" ")[0]




