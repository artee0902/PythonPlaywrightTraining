import pytest
from playwright.sync_api import sync_playwright

def test_select_date():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Navigate to the Bootstrap Date Picker Demo page
        page.goto("https://www.lambdatest.com/selenium-playground/bootstrap-date-picker-demo")

        # Click on the 'Start date' input field to open the calendar
        page.click("input[placeholder='Start date']")

        # Define locators for the calendar components
        date_picker_switch = page.locator("(//table[@class='table-condensed']//th[@class='datepicker-switch'])[1]")
        prev_button = page.locator("(//table[@class='table-condensed']//th[@class='prev'])[1]")

        # Target month and year
        target_month_year = "May 2019"

        # Navigate to the desired month and year
        while True:
            current_month_year = date_picker_switch.inner_text()
            if current_month_year == target_month_year:
                break
            prev_button.click()

        # Select the 4th day
        page.click("//td[@class='day' and text()='4']")

        # Verify that the input field has the correct date (DD/MM/YYYY format)
        selected_date = page.locator("input[placeholder='Start date']").input_value()
        assert selected_date == "04/05/2019", f"Expected date to be '04/05/2019' but got '{selected_date}'"

        browser.close()
