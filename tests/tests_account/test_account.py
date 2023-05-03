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
    for firstname in ["", random_str("name", 5)]
    for lastname in ["", random_str("lastname", 5)]
    for address in ["", random_str("address", 5)]
]

account_test_data2 = [
    AccountData(email=email, email2=email2, email3=email3)
    for email in ["", "tesmail@gmail.com"]
    for email2 in ["", "tesmail@gmail.com"]
    for email3 in ["", "tesmail@gmail.com"]
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


@pytest.mark.parametrize("account", account_test_data, ids=[repr(x) for x in account_test_data])
def test_edit_some_accounts(app, account):
    if not app.account_helper.count_of_accounts():
        app.account_helper.create_account(AccountData())

    old_accounts = app.account_helper.get_accounts()
    index = randrange(len(old_accounts))
    account.id = old_accounts[index].id

    app.account_helper.edit_some_account_by_index(account, index)
    edition_account_at_home_page = app.account_helper.get_account_by_id(account.id)

    new_accounts = app.account_helper.get_accounts()
    old_accounts[index] = edition_account_at_home_page

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

    # Check phones
    assert all_phones_from_home_page == app.account_helper.merge_phones_like_at_home_page(all_phones_from_edit_page)

    # Check names
    assert account_at_edit_page.firstname == account_at_home_page.firstname
    assert account_at_edit_page.lastname == account_at_home_page.lastname

    # Check address
    assert account_at_edit_page.address == account_at_home_page.address


@pytest.mark.parametrize("account", account_test_data2, ids=[repr(x) for x in account_test_data])
def test_check_emails_from_home_page_and_edit_page(app, account):
    app.account_helper.create_account(account)
    count_of_accounts = int(app.account_helper.get_count_of_accounts_from_home_page())
    random_account = random.randrange(count_of_accounts)

    account_at_home_page = app.account_helper.get_accounts()[random_account]
    account_at_edit_page = app.account_helper.get_account_data_from_edit_page_by_index(random_account)

    all_emails_from_home_page = account_at_home_page.all_emails_from_home_page
    all_emails_from_edit_page = account_at_edit_page

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
