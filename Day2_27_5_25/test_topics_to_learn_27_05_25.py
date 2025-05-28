import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module")
def page():
    print("Setting up Playwright and launching browser for Myntra...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Change to True for headless
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.flipkart.com/")
        yield page  # Provide the page to tests
        print("Closing browser...")
        browser.close()


def test_locator1(page):
    css_selector=page.locator(".Pke_EE")
    assert css_selector.is_visible(),"Cart should be visible"
    css_selector.fill("footwear")
    css_selector.press("Enter")



def test_extract_element_text(page):
    relevance=page.locator("//div[@class='zg-M3Z _0H7xSG']")
    rel_text=relevance.inner_text()  #for relevance word extract
    print(rel_text)


def test_extract_multiple_elements(page):
    sort_by=page.locator(".zg-M3Z")   #for sort by titles class locator is used
    sort_by_text=sort_by.all_inner_texts()
    count_sort_by = sort_by.count()
    print(count_sort_by)  #returns count of all sort by titles
    for i in sort_by_text:
        print(i)      #returns all sort by titles

def test_wait_dynamically_new_page(page):
    print("Testing dynamic wait for a new page...")

    # Click on a link or button that opens a new page or triggers a dynamic change
    # (Modify selector as per real UI element. Below is an example.)
    page.click("text=Mobiles")  # This should trigger navigation or content change

    # Wait for a specific element on the new page to be visible
    page.wait_for_selector("//span[normalize-space()='CATEGORIES']")  # Flipkart's product grid container

    # Assert that product grid is visible, indicating page has loaded
    assert page.locator("//span[normalize-space()='CATEGORIES']").is_visible(), "Product grid not visible after navigation"








