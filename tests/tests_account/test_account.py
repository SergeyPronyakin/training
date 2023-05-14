# -*- coding: utf-8 -*-
from random import randrange
import random
from model.account import AccountData


def test_create_account(app, db, json_accounts, check_ui):
    account = json_accounts
    old_accounts_from_ui = app.account_helper.get_accounts()
    old_accounts_from_bd = db.get_accounts()
    app.account_helper.create_account(account)
    new_accounts_from_db = db.get_accounts()

    account.all_phones_from_home_page = app.account_helper.merge_phones_like_at_home_page(account)
    account.all_emails_from_home_page = app.account_helper.merge_emails_like_at_home_page(account)
    new_account = AccountData(firstname=account.firstname, lastname=account.lastname, address=account.address,
                              all_emails_from_home_page=account.all_emails_from_home_page,
                              all_phones_from_home_page=account.all_phones_from_home_page)

    old_accounts_from_bd.append(account)
    assert sorted(old_accounts_from_bd, key=AccountData.id_or_max) == sorted(new_accounts_from_db, key=AccountData.id_or_max)

    if check_ui:
        old_accounts_from_ui.append(new_account)
        new_accounts_from_ui = app.account_helper.get_accounts()
        assert sorted(new_accounts_from_ui, key=AccountData.id_or_max) == sorted(old_accounts_from_ui, key=AccountData.id_or_max)


def test_delete_one_account(app, db, check_ui):
    if not db.get_accounts():
        app.account_helper.create_account(AccountData())

    count_of_accounts_before_deleting = int(app.account_helper.get_count_of_accounts_from_home_page())
    old_accounts = db.get_accounts()
    account = random.choice(old_accounts)
    app.account_helper.delete_account_by_id(str(account.id))
    new_accounts = db.get_accounts()
    old_accounts.remove(account)
    assert sorted(old_accounts, key=AccountData.id_or_max) == sorted(new_accounts, key=AccountData.id_or_max)

    if check_ui:
        new_accounts = app.account_helper.get_accounts()
        count_of_accounts_after_deleting = int(app.account_helper.get_count_of_accounts_from_home_page())
        assert count_of_accounts_before_deleting == count_of_accounts_after_deleting + 1
        assert sorted(new_accounts, key=AccountData.id_or_max) == sorted(old_accounts, key=AccountData.id_or_max)


def test_edit_some_accounts(app, json_accounts):
    account = json_accounts
    if not app.account_helper.count_of_accounts():
        app.account_helper.create_account(AccountData())

    old_accounts = app.account_helper.get_accounts()
    index = randrange(len(old_accounts))
    account.id = old_accounts[index].id

    edition_account = app.account_helper.edit_some_account_by_index(account, index)
    new_accounts = app.account_helper.get_accounts()

    edition_account.all_phones_from_home_page = app.account_helper.merge_phones_like_at_home_page(edition_account)
    edition_account.all_emails_from_home_page = app.account_helper.merge_emails_like_at_home_page(edition_account)
    edition_account = AccountData(id=account.id, firstname=edition_account.firstname, lastname=edition_account.lastname,
                                  address=edition_account.address,
                                  all_emails_from_home_page=account.all_emails_from_home_page,
                                  all_phones_from_home_page=account.all_phones_from_home_page)

    old_accounts[index] = edition_account
    assert sorted(old_accounts, key=AccountData.id_or_max) == sorted(new_accounts, key=AccountData.id_or_max)


def test_assert_random_account_data_from_home_page_and_edit_page(app):
    if not app.account_helper.count_of_accounts():
        app.account_helper.create_account(AccountData())

    count_of_accounts = int(app.account_helper.get_count_of_accounts_from_home_page())
    random_account = random.randrange(count_of_accounts)

    account_at_home_page = app.account_helper.get_accounts()[random_account]
    account_at_edit_page = app.account_helper.get_account_data_from_edit_page_by_index(random_account)

    all_phones_from_home_page = account_at_home_page.all_phones_from_home_page
    all_phones_from_edit_page = account_at_edit_page

    all_emails_from_home_page = account_at_home_page.all_emails_from_home_page
    all_emails_from_edit_page = account_at_edit_page

    # Check phones
    assert all_phones_from_home_page == app.account_helper.merge_phones_like_at_home_page(all_phones_from_edit_page)

    # Check names
    assert account_at_edit_page.firstname == account_at_home_page.firstname
    assert account_at_edit_page.lastname == account_at_home_page.lastname

    # Check address
    assert account_at_edit_page.address == account_at_home_page.address

    # Check emails
    assert all_emails_from_home_page == app.account_helper.merge_emails_like_at_home_page(all_emails_from_edit_page)


def test_delete_all_accounts(app):
    if not app.account_helper.count_of_accounts():
        app.account_helper.create_account(AccountData())

    count_of_accounts_before_deleting = int(app.account_helper.get_count_of_accounts_from_home_page())
    old_accounts = app.account_helper.get_accounts()

    app.account_helper.delete_all_at_ones_accounts()

    count_of_accounts_after_deleting = int(app.account_helper.get_count_of_accounts_from_home_page())

    assert app.account_helper.count_of_accounts() == 0
    assert len(old_accounts) > 0
    assert count_of_accounts_before_deleting >= count_of_accounts_after_deleting
    assert count_of_accounts_after_deleting == 0
