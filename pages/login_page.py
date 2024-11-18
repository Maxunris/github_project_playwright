from playwright.async_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.login_field = "#login_field"
        self.password_field = "#password"
        self.sign_in_button = 'input[value="Sign in"]'
        self.base_url = "https://github.com/login"
        self.incorrect_log_of_pass = "#js-flash-container"  # Локатор для контейнера ошибки
        self.error_message_text = "Incorrect username or password."

    async def goto(self):
        await self.page.goto(self.base_url)

    async def login(self, username: str, password: str):
        await self.page.fill(self.login_field, username)
        await self.page.fill(self.password_field, password)
        await self.page.locator(self.sign_in_button).click()

    async def is_logged_in(self):
        current_url = self.page.url
        return current_url == "https://github.com/"

    async def is_error_displayed(self):
        if await self.page.is_visible(self.incorrect_log_of_pass):
            error_message = await self.page.inner_text(self.incorrect_log_of_pass)
            return self.error_message_text in error_message
        return False
