from playwright.async_api import expect


class ProfilePage:
    def __init__(self, page):
        self.page = page

    async def verify_no_public_repositories(self):
        await expect(self.page.locator("#user-repositories-list")).to_contain_text(
            "doesn’t have any public repositories yet."
        )
