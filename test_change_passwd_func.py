#!/usr/bin/env python

import pytest

from change_passwd_func import change_passwd_func

OLD_PASSWD = 'OLD'

VALID_BASE_PASSWD_LEN4 = '1aB!'

@pytest.mark.parametrize('length', [0, 3, 17])
def test_change_passwd_func_less_length_0(length):
    assert not change_passwd_func(OLD_PASSWD, 'a'*length)
    # assert change_passwd_func(OLD_PASSWD, new_passwd)

@pytest.mark.parametrize('length', [18, 19])
def test_change_passwd_func_enough_length_18(length):
    new_passwd = VALID_BASE_PASSWD_LEN4.zfill(length)
    assert change_passwd_func(OLD_PASSWD, new_passwd)

@pytest.mark.parametrize('invalid_char', ['-'])
def test_change_passwd_func_invalid_char(invalid_char):
    new_passwd = '{}{}'.format(VALID_BASE_PASSWD_LEN4.zfill(18), invalid_char)
    assert not change_passwd_func(OLD_PASSWD, new_passwd)

@pytest.mark.parametrize('special_char', ['!', '@', '#', '$', '&', '*'])
def test_change_passwd_func_valid_special_char(special_char):
    new_passwd = '{}{}'.format(VALID_BASE_PASSWD_LEN4.zfill(18), special_char)
    assert change_passwd_func(OLD_PASSWD, new_passwd)
