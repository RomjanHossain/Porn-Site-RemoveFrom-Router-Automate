from playwright.sync_api import Playwright, expect, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # login
    page.goto("http://192.168.69.69/")
    page.goto("http://192.168.69.69/login.htm")
    page.locator("#username").fill("romjan1412")
    page.locator("#password").click()
    page.locator("#password").fill("python")
    page.get_by_role("button", name="Login").click()
    # goto blocking section

    with open("sites.txt", "r") as f:
        page.wait_for_timeout(1000)
        for link in f.readlines():
            page.frame_locator('frame[name="main"]').get_by_role(
                "link", name="Advanced"
            ).click()
            page.frame_locator('frame[name="main"]').get_by_role(
                "link", name="URL Block"
            ).click()
            # this is text box select and click apply
            page.wait_for_timeout(1000)
            page.frame_locator('frame[name="main"]').get_by_role("textbox").click()
            if "www." in link:
                link = link.replace("www.", "")
            page.frame_locator('frame[name="main"]').get_by_role("textbox").fill(link)
            page.frame_locator('frame[name="main"]').get_by_role(
                "button", name="AddKeyword"
            ).click()
            page.wait_for_timeout(9000)
            page.reload()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
