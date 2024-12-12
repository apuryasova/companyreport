from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def click_menu_item(self, menu_name: str):
        self.page.get_by_role("link", name=menu_name).click()

    def wait_for_text(self, text: str):
        text = text.strip()  # Убираем лишние пробелы
        self.page.wait_for_selector(f"text={text}")
