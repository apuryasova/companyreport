import pytest
from playwright.sync_api import sync_playwright, Browser, Page


@pytest.fixture(params=["chromium", "firefox", "webkit"], scope="session")
def browser(request):
    with sync_playwright() as playwright:
        browser = getattr(playwright, request.param).launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def page(browser: Browser) -> Page:
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()