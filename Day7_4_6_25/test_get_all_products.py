from playwright.sync_api import Playwright

from utils.utils import APIUtils


def test_e2e_web_api(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    contest=browser.new_context()
    page=contest.new_page()


    #get_all_products

    products=APIUtils()
    products.get_all_prducts(playwright)


    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("aartigorde999@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Aarti@9420")
    page.get_by_role("button",name="Login")
    page.wait_for_load_state("networkidle")