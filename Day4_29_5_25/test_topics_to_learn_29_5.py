#Write the Script to dynamically find the product to buy from lists of products
import time

import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://rahulshettyacademy.com/client"
EMAIL = "aartigorde999@gmail.com"
PASSWORD = "Aati@9420"
PRODUCT_NAME = "zara coat 3"




@pytest.fixture
def setup(page):
    page.goto(BASE_URL)
    page.get_by_placeholder("email@example.com").fill(EMAIL)
    page.get_by_placeholder("enter your passsword").fill(PASSWORD)
    page.get_by_role("button",name="Login").click()
    page.wait_for_timeout(3000)

def test_add_product_to_cart(page:Page,setup):
    expect(page.get_by_text("IPHONE 13 PRO")).to_be_visible()
    page.get_by_role("button",name=" Add To Cart").click()








