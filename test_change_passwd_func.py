#!/usr/bin/env python

import pytest

from change_passwd_func import change_passwd_func

OLD_PASSWD = 'OLD'

@pytest.mark.parametrize('new_passwd', ['', 'abc', 'a'*17])
def test_change_passwd_func_less_length_0(new_passwd):
    assert not change_passwd_func(OLD_PASSWD, new_passwd)

@pytest.mark.parametrize('new_passwd', ['a'*18, 'a'*19])
def test_change_passwd_func_enough_length_18(new_passwd):
    assert change_passwd_func(OLD_PASSWD, new_passwd)
