class CreateRepoPage:
    def __init__(self, page):
        self.page = page

    async def fill_repository_details(self, repo_name, description):
        await self.page.get_by_test_id("repository-name-input").fill(repo_name)
        await self.page.get_by_label("Description").fill(description)

    async def add_readme(self):
        await self.page.get_by_label("Add a README file").check()

    async def select_gitignore_template(self, template_name):
        await self.page.get_by_role("button", name=".gitignore template: None").click()
        await self.page.get_by_placeholder("Filter…").fill(template_name)
        await self.page.get_by_text(template_name).click()

    async def create_repository(self):
        await self.page.get_by_text("Create repository").click()
