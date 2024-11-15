import time

import pytest

@pytest.mark.asyncio
async def test_authenticated_page(browser_with_cookies):
    """Тест аутентифицированной страницы"""
    page = browser_with_cookies
    await page.goto("https://github.com/")

    time.sleep(10)
