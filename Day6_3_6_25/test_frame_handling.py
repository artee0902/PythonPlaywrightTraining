import time

import pytest
from playwright.sync_api import Page, expect



@pytest.fixture
def setup(page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

#test_Case:1
def test_hide_show(page:Page,setup):
    expect(page.get_by_placeholder("Enter Your Name")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    time.sleep(2)
    expect(page.get_by_placeholder("Enter Your Name")).not_to_be_hidden()


    page.get_by_role("button", name="Show").click()
    time.sleep(2)
    expect(page.get_by_placeholder("Enter Your Name")).to_be_visible()


#test_case:2
def test_dialog_box(page:Page,setup):
    page.on("dialog",lambda dialog:dialog.accept())
    time.sleep(3)
    page.get_by_role("button", name="Confirm").click()
    time.sleep(3)

def test_frame_handle(page:Page,setup):
    pageFrame=page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link",name="All Access plan").click()
    expect(pageFrame.locator("body")).to_contain_text(" Happy Subscibers!")



