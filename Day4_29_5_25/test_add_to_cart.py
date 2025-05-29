import pytest
from playwright.sync_api import Page, expect
import time

# --- Configurable constants ---
EMAIL = "aartigorde999@gmail.com"
PASSWORD = "Aarti@9420"
PRODUCT_NAME = "IPHONE 13 PRO"
BASE_URL = "https://rahulshettyacademy.com/client"


def delay(ms):
    time.sleep(ms / 1000)


@pytest.mark.order(1)
def test_e2e_order_flow(page: Page):
    # Step 1: Visit login page
    page.goto(BASE_URL)
    delay(1500)

    # Step 2: Login
    page.fill("#userEmail", EMAIL)
    delay(1000)
    page.fill("#userPassword", PASSWORD)
    delay(1000)
    page.click("input[value='Login']")
    page.wait_for_load_state("networkidle")
    delay(2000)

    # Step 3: Wait for products to load
    products = page.locator(".card-body")
    products.first.wait_for()
    delay(1000)

    # Step 4: Find product and add to cart
    count = products.count()
    product_found = False
    for i in range(count):
        title = products.nth(i).locator("b").text_content().strip().upper()
        if title == PRODUCT_NAME:
            products.nth(i).locator("text= Add To Cart").click()
            product_found = True
            delay(1500)
            break
    assert product_found, f"{PRODUCT_NAME} not found on the product page."

    # Step 5: Go to cart and verify product
    page.click("[routerlink*='cart']")
    page.locator("div li").first.wait_for()
    delay(1500)
    is_visible = page.locator(f"h3:has-text('{PRODUCT_NAME}')").is_visible()
    assert is_visible, f"{PRODUCT_NAME} not found in cart."

    # Step 6: Checkout
    page.click("text=Checkout")
    delay(1500)

    # Step 7: Select country from dropdown
    page.type("[placeholder*='Country']", "ind", delay=100)
    delay(1500)
    dropdown = page.locator(".ta-results")
    dropdown.wait_for()
    options = dropdown.locator("button")
    for i in range(options.count()):
        if options.nth(i).text_content().strip() == "India":
            options.nth(i).click()
            delay(1500)
            break

    # Step 8: Verify email field is auto-filled
    expect(page.locator(".user__name input[type='text']")).to_have_value(EMAIL)
    delay(1000)

    # Step 9: Submit order
    page.click(".action__submit")
    delay(2000)

    # Step 10: Verify order confirmation
    expect(page.locator(".hero-primary")).to_have_text(" Thankyou for the order. ")
    order_id = page.locator(".em-spacer-1 .ng-star-inserted").text_content().strip()
    print("✅ Order ID:", order_id)
    delay(1500)

    # Step 11: Go to My Orders and verify order exists
    page.click("button[routerlink*='myorders']")
    page.locator("tbody").wait_for()
    delay(2000)
    rows = page.locator("tbody tr")
    found_order = False

    for i in range(rows.count()):
        row_id = rows.nth(i).locator("th").text_content().strip()
        print(f"Checking row {i + 1}: {row_id}")
        if order_id.startswith(row_id):
            rows.nth(i).locator("button").first.click()
            delay(1500)
            found_order = True
            break

    if not found_order:
        print("❌ Order not found in history! Screenshot saved.")
        page.screenshot(path="order_history_failure.png", full_page=True)

    assert found_order, f"Order {order_id} not found in history."

    # Step 12: Verify order details in modal
    order_id_details = page.locator(".col-text").text_content().strip()
    assert order_id in order_id_details, "Order ID mismatch in order detail modal."
    print("✅ Order verified successfully.")
    delay(1500)
