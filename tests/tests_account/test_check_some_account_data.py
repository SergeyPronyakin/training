import random
from model.account import AccountData


def test_check_some_account_data(app):
    if not app.account_helper.count_of_accounts():
        app.account_helper.create_account(AccountData())

    count_of_accounts = int(app.account_helper.get_accounts_count_from_page())
    random_account = random.randrange(count_of_accounts)

    account_at_home_page = app.account_helper.accounts()[random_account]
    account_at_edit_page = app.account_helper.get_account_data_from_edit_page_by_index(random_account)

    all_phones_from_home_page = account_at_home_page.all_phones_from_home_page
    all_phones_from_edit_page = account_at_edit_page

    all_emails_from_home_page = account_at_home_page.all_emails_from_home_page
    all_emails_from_edit_page = account_at_edit_page

    # Check phones
    assert all_phones_from_home_page == app.account_helper.merge_phones_like_at_home_page(all_phones_from_edit_page)

    # Check emails
    assert all_emails_from_home_page == app.account_helper.merge_emails_like_at_home_page(all_emails_from_edit_page)

    # Check names
    assert account_at_edit_page.firstname == account_at_home_page.firstname
    assert account_at_edit_page.lastname == account_at_home_page.lastname

    # Check address
    assert account_at_edit_page.address == account_at_home_page.address

