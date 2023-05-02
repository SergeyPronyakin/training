# -*- coding: utf-8 -*-
from random import randrange
import random
import string

import pytest

from model.account import AccountData


def random_str(prefix, maxlen):
    symbols = string.ascii_letters # + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_int(min, max):
    return "".join(random.choice("0123456789") for i in range(random.randint(min, max)))


def random_phone():
    phone = []
    country_codes = [random_int(1, 2)]
    city_codes = [random_int(1, 4)]
    random_index = int(random.choice("01"))
    prefs = ["", "+"][random_index]
    parenthesis_open = ["", "("][random_index]
    phone_bodies = [random_int(4, 8)]
    for a, b, c, d, e in zip(prefs, country_codes, parenthesis_open, city_codes, phone_bodies):
        phone.append(a)
        phone.append(b)
        phone.append(c)
        phone.append(d)
        if c:
            phone.append(")")
            print(phone)
        phone.append(e)

    return "".join(phone)


account_test_data = [
    AccountData(firstname=firstname, lastname=lastname, address=address)
    for firstname in ["", random_str("name", 25)]
    for lastname in ["", random_str("lastname", 25)]
    for address in ["", random_str("address", 25)]
]


@pytest.mark.parametrize("account", account_test_data, ids=[repr(x) for x in account_test_data])
def test_create_account(app, account):
    old_accounts = app.account_helper.get_accounts()
    new_account = app.account_helper.create_account(account)
    new_accounts = app.account_helper.get_accounts()

    assert app.account_helper.count_of_accounts() == len(old_accounts) + 1
    old_accounts.append(new_account)
    assert sorted(new_accounts, key=AccountData.id_or_max) == sorted(old_accounts, key=AccountData.id_or_max)


def test_delete_one_account(app):
    if not app.account_helper.count_of_accounts():
        app.account_helper.create_account(AccountData())

    count_of_accounts_before_deleting = int(app.account_helper.get_count_of_accounts_from_home_page())
    old_accounts = app.account_helper.get_accounts()

    index = randrange(len(old_accounts))
    app.account_helper.delete_account_by_index(index)
    new_accounts = app.account_helper.get_accounts()

    count_of_accounts_after_deleting = int(app.account_helper.get_count_of_accounts_from_home_page())

    assert len(old_accounts) == app.account_helper.count_of_accounts() + 1
    assert count_of_accounts_before_deleting == count_of_accounts_after_deleting + 1
    old_accounts[index:index + 1] = []
    assert sorted(new_accounts, key=AccountData.id_or_max) == sorted(old_accounts, key=AccountData.id_or_max)


def test_edit_some_accounts(app):
    assert_data = ''.join(random.choices(string.ascii_lowercase, k=5))
    if not app.account_helper.count_of_accounts():
        app.account_helper.create_account(AccountData())

    old_accounts = app.account_helper.get_accounts()
    index = randrange(len(old_accounts))
    account_data = AccountData(firstname=assert_data, lastname=assert_data)
    account_data.id = old_accounts[index].id

    app.account_helper.edit_some_account_by_index(account_data, index)
    new_accounts = app.account_helper.get_accounts()
    old_accounts[index] = account_data

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

    # Check emails
    assert all_emails_from_home_page == app.account_helper.merge_emails_like_at_home_page(all_emails_from_edit_page)

    # Check names
    assert account_at_edit_page.firstname == account_at_home_page.firstname
    assert account_at_edit_page.lastname == account_at_home_page.lastname

    # Check address
    assert account_at_edit_page.address == account_at_home_page.address


def test_delete_all_accounts(app):
    if not app.account_helper.count_of_accounts():
        app.account_helper.create_account(AccountData())

    count_of_accounts_before_deleting = int(app.account_helper.get_count_of_accounts_from_home_page())
    old_accounts = app.account_helper.get_accounts()

    app.account_helper.delete_all_accounts()

    count_of_accounts_after_deleting = int(app.account_helper.get_count_of_accounts_from_home_page())

    assert app.account_helper.count_of_accounts() == 0
    assert len(old_accounts) > 0
    assert count_of_accounts_before_deleting >= count_of_accounts_after_deleting
    assert count_of_accounts_after_deleting == 0
