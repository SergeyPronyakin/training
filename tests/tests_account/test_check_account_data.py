import random
import time

from model.account import AccountData


def test_edit_some_accounts(app):
    if not app.account_helper.count_of_accounts():
        app.account_helper.create_account(AccountData())

    count_of_accounts = int(app.account_helper.get_accounts_count_from_page())
    random_account = random.randrange(count_of_accounts)

    print(app.account_helper.get_account_data_from_edit_page_by_index(random_account))
    print(app.account_helper.accounts()[random_account])
