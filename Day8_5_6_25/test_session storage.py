from playwright.sync_api import sync_playwright

def test_session_storage_reuse_rahulshetty():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        # Step 1: Login and set session storage
        context1 = browser.new_context()
        page1 = context1.new_page()
        page1.goto("https://rahulshettyacademy.com/loginpagePractise/")

        # Perform login
        page1.get_by_label("Username:").fill("rahulshettyacademy")
        page1.get_by_label("Password:").fill("learning")
        page1.get_by_role("combobox").select_option("Teacher")
        page1.locator("#terms").check()
        page1.get_by_role("button", name="Sign In").click()
        page1.wait_for_url("**/angularpractice/shop")  # Wait for login redirect

        # Optionally store a session value manually to test
        page1.evaluate("sessionStorage.setItem('customToken', 'abc123')")

        # Step 2: Save sessionStorage
        session_data = page1.evaluate("""() => {
            const data = {};
            for (let i = 0; i < sessionStorage.length; i++) {
                const key = sessionStorage.key(i);
                data[key] = sessionStorage.getItem(key);
            }
            return data;
        }""")

        print("Saved sessionStorage:", session_data)
        context1.close()

        # Step 3: New context and inject sessionStorage
        context2 = browser.new_context()
        page2 = context2.new_page()
        page2.goto("https://rahulshettyacademy.com/loginpagePractise/")

        page2.evaluate("""(data) => {
            for (const key in data) {
                sessionStorage.setItem(key, data[key]);
            }
        }""", session_data)

        # Step 4: Reload and verify
        page2.reload()
        restored_value = page2.evaluate("sessionStorage.getItem('customToken')")
        print("Restored sessionStorage value:", restored_value)
        assert restored_value == "abc123"

        browser.close()
