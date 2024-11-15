from playwright.async_api import expect


class MainPageRepo:
    def __init__(self, page):
        self.page = page

    async def verify_repository_created(self, repo_name, description):
        await expect(self.page.locator("#repo-title-component")).to_contain_text(repo_name)
        await expect(self.page.locator("#folder-row-0")).to_contain_text(".gitignore")
        await expect(self.page.locator("#folder-row-1")).to_contain_text("README.md")
        await expect(self.page.get_by_role("article")).to_contain_text(description)
