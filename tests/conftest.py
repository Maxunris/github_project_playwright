import pytest_asyncio
from dotenv import load_dotenv
from playwright.async_api import async_playwright
import os

@pytest_asyncio.fixture(scope="function", autouse=True)
def load_env():
    load_dotenv()

@pytest_asyncio.fixture(scope="session")
async def browser_context():
    load_dotenv()
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        base_url = 'https://github.com/login'
        page = await context.new_page()
        await page.goto(base_url)

        login = os.getenv('LOGIN')
        password = os.getenv('PASSWORD')

        if not login or not password:
            raise ValueError("Переменные LOGIN и PASSWORD должны быть определены в .env")

        await page.fill("#login_field", login)
        await page.fill("#password", password)
        await page.locator('input[value="Sign in"]').click()
        await page.wait_for_timeout(2000)
        cookies = await context.cookies()

        await browser.close()
        return cookies

@pytest_asyncio.fixture(scope="function")
async def browser_with_cookies(browser_context):
    """Открывает браузер с сохраненными cookies"""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            viewport={"width": 1920, "height": 1080})
        await context.add_cookies(browser_context)
        page = await context.new_page()
        try:
            yield page
        finally:
            await context.close()
            await browser.close()