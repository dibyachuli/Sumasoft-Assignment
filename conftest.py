import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope='function')
def page():
    with sync_playwright() as d:
        browser = d.chromium.launch(headless=False)
        page=browser.new_page()
        yield page
        browser.close()