import pytest
from pages.login_page import LoginPage

TEST_DATA = [
    ("Max1@gmail.com", "Allods123", "Incorrect username or password."),
    ("Max2@gmail.com", "Allods1245", "Incorrect username or password."),
    ("Max3@gmail.com", "Allods125125", "Incorrect username or password."),
    ("Max4@gmail.com", "Allods11221123", "Incorrect username or password.")
]
@pytest.mark.negative
@pytest.mark.parametrize("username,password,expected_error", TEST_DATA)
@pytest.mark.asyncio
async def test_negative_login(browser_without_cookies, username, password, expected_error):
    page = browser_without_cookies
    login_page = LoginPage(page)
    await login_page.goto()

    await login_page.login(username, password)

    assert await login_page.is_error_displayed(), f"Сообщение об ошибке не отображается при логине '{username}'"
    error_text = await page.inner_text(login_page.incorrect_log_of_pass)
    assert expected_error in error_text, f"Ожидалось '{expected_error}', но было '{error_text}'"
