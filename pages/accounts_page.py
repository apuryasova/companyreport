import time
from pages.base_page import BasePage


class AccountsPage(BasePage):
    def create_account(self, account_name: str, phone: str):
        self.click_menu_item("Marketing")
        self.click_menu_item("Accounts")
        self.click_menu_item(" Create Account")
        self.page.locator("#name").fill(account_name)
        self.page.locator("#phone_office").fill(phone)
        self.page.get_by_role("cell", name="Save Cancel").locator("#SAVE").click()
        self.wait_for_text(account_name)
        time.sleep(10)

    def link_lead_to_account(self, account_name: str, lead_name: str):
        self.click_menu_item("Marketing")
        self.click_menu_item("Accounts")
        # Локатор для первого элемента списка "Recently Viewed"
        self.page.locator("div#recentlyViewedSidebar li.recentlinks a[accesskey='1']").click()

        # Переход на вкладку Leads
        self.page.locator("a#subpanel_title_leads[role='button']").scroll_into_view_if_needed()
        self.page.locator("a#subpanel_title_leads[role='button']").click()

        # Проверка, что панель открылась
        self.page.wait_for_selector("#subpanel_leads", state="visible")

        # Нажимаем Select в выпадающем списке
        self.page.locator("#account_leads_select_button").click()

        # Работа с всплывающим окном для выбора лида
        with self.page.expect_popup() as popup_info:
            self.page.locator("span.suitepicon-action-caret").click()  # Раскрываем список
        popup_page = popup_info.value

        # Выбор лида и подтверждение
        popup_page.get_by_role("row", name=f" {lead_name}").get_by_role("checkbox").check()
        popup_page.locator("a#account_leads_select_button").click()  # Нажимаем Select
        self.wait_for_text(lead_name)
