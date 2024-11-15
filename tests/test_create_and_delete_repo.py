import os
import time

import pytest
from playwright.async_api import expect

@pytest.mark.asyncio
async def test_create_repo(browser_with_cookies):
    page = browser_with_cookies
    try:
        await page.goto("https://github.com/new")
        await page.get_by_test_id("repository-name-input").fill("testnewrepo")
        await page.get_by_label("Description").fill("testdescription")
        await page.get_by_label("Add a README file").check()
        await page.get_by_role("button", name=".gitignore template: None").click()
        await page.get_by_placeholder("Filter…").fill("py")
        await page.get_by_text("Python").click()
        time.sleep(3)
        await page.get_by_text("Create repository").click()

        await expect(page.locator("#repo-title-component")).to_contain_text("testnewrepo")
        await expect(page.locator("#folder-row-0")).to_contain_text(".gitignore")
        await expect(page.locator("#folder-row-1")).to_contain_text("README.md")
        await expect(page.get_by_role("article")).to_contain_text("testdescription")

    except Exception as e:
        os.makedirs("screenshots", exist_ok=True)
        await page.screenshot(path="screenshots/test_create_repo_error.png")
        print(f"Ошибка в test_create_repo: {e}")
        raise

@pytest.mark.asyncio
async def test_delete_repo(browser_with_cookies):
    page = browser_with_cookies
    try:
        await page.goto("https://github.com/maxtest2451/testnewrepo/settings")
        await page.get_by_role("button", name="Delete this repository").click()
        await page.get_by_label("Effects of deleting this").get_by_text("maxtest2451/testnewrepo").click()
        await page.get_by_role("button", name="I want to delete this").click()
        await page.get_by_role("button", name="I have read and understand").click()
        await page.get_by_label("To confirm, type \"maxtest2451").fill("maxtest2451/testnewrepo")
        await page.get_by_label("Delete maxtest2451/testnewrepo").get_by_role("button", name="Delete this repository").click()

        await expect(page.locator("#user-repositories-list")).to_contain_text("maxtest2451 doesn’t have any public repositories yet.")

    except Exception as e:
        os.makedirs("screenshots", exist_ok=True)
        await page.screenshot(path="screenshots/test_delete_repo_error.png")
        print(f"Ошибка в test_delete_repo: {e}")
        raise
