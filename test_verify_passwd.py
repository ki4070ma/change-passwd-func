#!/usr/bin/env python

import pytest

from verify_passwd import verify_passwd
from helper.helper import VALID_BASE_PASSWD_LEN4, str_padding

@pytest.mark.parametrize('length', [0, 3, 17])
def test_change_passwd_func_less_length_0(length):
    assert not verify_passwd('a'*length)

@pytest.mark.parametrize('length', [18, 19])
def test_change_passwd_func_enough_length_18(length):
    new_passwd = str_padding(VALID_BASE_PASSWD_LEN4, length)
    assert verify_passwd(new_passwd)

@pytest.mark.parametrize('invalid_char', ['-'])
def test_change_passwd_func_invalid_char(invalid_char):
    new_passwd = str_padding(invalid_char)
    assert not verify_passwd(new_passwd)

@pytest.mark.parametrize('special_char', ['!', '@', '#', '$', '&', '*'])
def test_change_passwd_func_valid_special_char(special_char):
    new_passwd = str_padding(special_char)
    assert verify_passwd(new_passwd)

@pytest.mark.parametrize('continous_num', [3])
def test_change_password_func_continuous_3_num(continous_num):
    new_passwd = str_padding('a'*continous_num)
    assert verify_passwd(new_passwd)

@pytest.mark.parametrize('continous_num', [4, 5])
def test_change_password_func_continuous_3_num(continous_num):
    new_passwd = str_padding('a'*continous_num)
    assert not verify_passwd(new_passwd)
