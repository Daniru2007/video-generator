from playwright.sync_api import Page, expect, sync_playwright


def take_screenshots(content):
    print("taking screenshots")
    with sync_playwright() as playwright:
        webkit = playwright.webkit
        browser = webkit.launch()
        context = browser.new_context()
        page = context.new_page()
        page.goto(content["url"])
        page.locator(content["id"]).screenshot(path="img/ss.png")
        content["path"] = "img/ss.png"

    for i, data in enumerate(content["data"]):
        with sync_playwright() as playwright:
            webkit = playwright.webkit
            browser = webkit.launch()
            context = browser.new_context()
            page = context.new_page()
            page.goto(data["url"])
            page.locator(data["id"]).screenshot(path=f"img/ss{i}.png")
            content["data"][i]["path"] = f"img/ss{i}.png"


if __name__ == "__main__":
    take_screenshots(content={"url": "https://www.youtube.com/"})
