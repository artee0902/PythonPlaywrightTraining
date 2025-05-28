import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module")
def page():
    print("Setting up Playwright and launching browser for Myntra...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Change to True for headless
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.myntra.com")
        yield page  # Provide the page to tests
        print("Closing browser...")
        browser.close()

def test_myntra_title(page):
    print("Checking Myntra page title...")
    assert "Myntra" in page.title()

def test_myntra_url(page):
    print("Checking Myntra URL...")
    assert page.url.startswith("https://www.myntra.com")


def test_search_footwear(page):
    print("Searching for 'footwear' on Myntra...")

    # Find the search bar and type "footwear"
    search_box = page.locator("input[placeholder='Search for products, brands and more']")
    search_box.click()
    search_box.fill("footwear")
    search_box.press("Enter")

    # Wait for results to load
    page.wait_for_selector("ul.results-base", timeout=10000)

    # Check that results page contains "footwear"
    assert "footwear" in page.url.lower()
    print("Search test passed!")