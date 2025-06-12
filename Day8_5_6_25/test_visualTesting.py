from playwright.sync_api import sync_playwright
from PIL import Image, ImageChops
import os
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

def compare_images(baseline_path, current_path):
    img1 = Image.open(baseline_path)
    img2 = Image.open(current_path)
    diff = ImageChops.difference(img1, img2)
    return diff.getbbox() is None  # No diff = images are visually the same

def test_visual_ecommerce_homepage():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Run without UI
        page = browser.new_page()
        page.goto("https://rahulshettyacademy.com/client/")

        os.makedirs("screenshots", exist_ok=True)
        baseline_path = "screenshots/baseline_ecommerce.png"
        current_path = "screenshots/current_ecommerce.png"

        # Take current screenshot
        page.screenshot(path=current_path, full_page=True)

        # Compare or Save baseline
        if not os.path.exists(baseline_path):
            page.screenshot(path=baseline_path, full_page=True)
            print("Baseline screenshot saved.")
        else:
            is_same = compare_images(baseline_path, current_path)
            if is_same:
                print("No visual changes detected.")
            else:
                print("Visual changes found! Check screenshots folder.")

        browser.close()

# Run the test
if __name__ == "__main__":
    test_visual_ecommerce_homepage()
