class DeleteRepoPage:
    def __init__(self, page):
        self.page = page

    async def delete_repository(self, repo_name):
        await self.page.get_by_role("button", name="Delete this repository").click()
        await self.page.get_by_label("Effects of deleting this").get_by_text(repo_name).click()
        await self.page.get_by_role("button", name="I want to delete this").click()
        await self.page.get_by_role("button", name="I have read and understand").click()
        await self.page.get_by_label(f"To confirm, type \"{repo_name}\"").fill(repo_name)
        await self.page.get_by_label(f"Delete {repo_name}").get_by_role("button", name="Delete this repository").click()
