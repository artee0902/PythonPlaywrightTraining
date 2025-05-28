from itertools import count

from playwright.sync_api import sync_playwright
import pytest


@pytest.fixture(scope="module")
def page():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        context=browser.new_context()
        page=context.new_page()
        page.goto("https://www.amazon.in/")
        yield page
        browser.close()

def test_drp(page):
    All_options=page.locator("select#searchDropdownBox")
    All_options.select_option("Books")

   # Verify if the selected option is "Books"
    selected = All_options.locator("option:checked").inner_text()
    print("Selected option:", selected)
    assert "Books" in selected


def test_check_box(page):
    mobiles=page.locator("//a[contains(text(), 'Mobiles')]")
    mobiles.click()
    # page.wait_for_timeout(3000)
    #
    # page.wait_for_selector("//span[text()='Brands']")
    #
    # check_box=page.locator("//label[@for='apb-browse-refinements-checkbox_3']//i[@class='a-icon a-icon-checkbox']")
    # check_box.check()
    #
    # assert "Samsung" in page.content()

    mobiles=page.locator("//div[@id='brandsRefinements']//span[@class='a-size-base a-color-base']")
    mobiles_text=mobiles.inner_text()
    count_mobiles=mobiles.count()
    print(count_mobiles)
    for i in mobiles_text:
        print(i)

