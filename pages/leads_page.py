from pages.base_page import BasePage


class LeadsPage(BasePage):
    def create_lead(self, salutation: str, first_name: str, last_name: str, phone: str):
        self.click_menu_item("Marketing")
        self.click_menu_item("Leads")
        self.click_menu_item(" Create Lead")
        self.page.locator("#salutation").select_option(salutation)
        self.page.locator("#first_name").fill(first_name)
        self.page.locator("#last_name").fill(last_name)
        self.page.locator("#phone_work").fill(phone)
        self.page.get_by_role("cell", name="Save Cancel").locator("#SAVE").click()
        self.wait_for_text(f"{salutation} {first_name} {last_name}")
