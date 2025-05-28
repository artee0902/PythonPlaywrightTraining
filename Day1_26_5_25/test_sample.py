# test_selenium_dev.py

def test_title_check(page):
    page.goto("https://www.selenium.dev/")
    assert page.title() == "Selenium"

def test_documentation_button_visibility(page):
    page.goto("https://www.selenium.dev/")
    doc_button = page.locator("//span[normalize-space()='Documentation']")
    assert doc_button.is_visible()

def test_projects_menu_visibility(page):
    page.goto("https://www.selenium.dev/")
    assert page.locator("text=Projects").is_visible()

def test_navigation_to_projects(page):
    page.goto("https://www.selenium.dev/")
    page.click("text=Projects")
    assert "projects" in page.url
