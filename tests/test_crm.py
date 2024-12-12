from faker import Faker
import pytest
from pages.login_page import LoginPage
from pages.leads_page import LeadsPage
from pages.accounts_page import AccountsPage

fake = Faker()


@pytest.fixture
def generated_data():
    """Генерирует уникальные данные для теста."""
    lead_first_name = fake.first_name()
    lead_last_name = fake.last_name()
    lead_phone = fake.phone_number()
    account_name = fake.company()
    account_phone = fake.phone_number()

    return {
        "lead_first_name": lead_first_name,
        "lead_last_name": lead_last_name,
        "lead_phone": lead_phone,
        "account_name": account_name,
        "account_phone": account_phone,
    }


def test_crm_flow(page, generated_data):
    login_page = LoginPage(page)
    login_page.login("test1", "Trust#@$123")

    # Генерация данных
    data = generated_data
    lead_name = f"Mr. {data['lead_first_name']} {data['lead_last_name']}"

    # Создание лида
    leads_page = LeadsPage(page)
    leads_page.create_lead("Mr.", data["lead_first_name"], data["lead_last_name"], data["lead_phone"])

    # Создание контрагента
    accounts_page = AccountsPage(page)
    accounts_page.create_account(data["account_name"], data["account_phone"])

    # Привязка лида к контрагенту
    accounts_page.link_lead_to_account(data["account_name"], lead_name)
