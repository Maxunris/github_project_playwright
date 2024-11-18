import os
import time
import pytest
from pages.create_repo_page import CreateRepoPage
from pages.main_page_repo import MainPageRepo
from pages.delete_repo_page import DeleteRepoPage
from pages.profile_page import ProfilePage
@pytest.mark.positive
@pytest.mark.asyncio
async def test_create_repo(browser_with_cookies):
    page = browser_with_cookies
    create_repo_page = CreateRepoPage(page)
    main_page_repo = MainPageRepo(page)

    try:
        await page.goto("https://github.com/new")
        await create_repo_page.fill_repository_details("testnewrepo", "testdescription")
        await create_repo_page.add_readme()
        await create_repo_page.select_gitignore_template("Python")
        time.sleep(1)
        await create_repo_page.create_repository()
        await main_page_repo.verify_repository_created("testnewrepo", "testdescription")

    except Exception as e:
        os.makedirs("screenshots", exist_ok=True)
        await page.screenshot(path="screenshots/test_create_repo_error.png")
        print(f"Ошибка в test_create_repo: {e}")
        raise
@pytest.mark.positive
@pytest.mark.asyncio
async def test_delete_repo(browser_with_cookies):
    page = browser_with_cookies
    delete_repo_page = DeleteRepoPage(page)
    profile_page = ProfilePage(page)
    repo_url = "https://github.com/maxtest2451/testnewrepo"

    try:
        await page.goto(f"{repo_url}/settings")
        await delete_repo_page.delete_repository("maxtest2451/testnewrepo")

        # Assertions
        await page.goto("https://github.com/maxtest2451?tab=repositories")
        await profile_page.verify_no_public_repositories()

    except Exception as e:
        os.makedirs("screenshots", exist_ok=True)
        await page.screenshot(path="screenshots/test_delete_repo_error.png")
        print(f"Ошибка в test_delete_repo: {e}")
        raise
