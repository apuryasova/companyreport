from pages.base_page import BasePage


class LoginPage(BasePage):
    def login(self, username: str, password: str):
        self.page.goto("https://crmqa.companyreport.net/index.php?action=Login&module=Users")
        self.page.get_by_role("textbox", name="Username").fill(username)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name="Log In").click()