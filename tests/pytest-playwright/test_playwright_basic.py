import pytest
from playwright.sync_api import Page, Playwright, sync_playwright


@pytest.fixture()
def setup(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False, slow_mo=500, args=["--start-maximized"])
    page = browser.new_page(no_viewport=True)
    page.goto("https://playwright.dev/python/")
    return page


def test_playwright_python_docs(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500, args=["--start-maximized"])
    page = browser.new_page(no_viewport=True)
    page.goto("https://playwright.dev/python/")
    page.locator('[class="navbar__item navbar__link"]', has_text='API').click()
    page.wait_for_timeout(3000)


def test_playwright_python_api(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500, args=["--start-maximized"])
    page = browser.new_page(no_viewport=True)
    page.goto("https://playwright.dev/python/docs/api/class-playwright")
    page.locator('[class="navbar__item navbar__link"]', has_text='Docs').click()
    page.wait_for_timeout(3000)
