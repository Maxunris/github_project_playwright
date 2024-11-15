import time

import pytest
from playwright.async_api import async_playwright

@pytest.mark.asyncio
async def test_authenticated_page(browser_with_cookies):
    """Тест аутентифицированной страницы"""
    page = browser_with_cookies
    await page.goto("https://github.com/")

    time.sleep(10)
