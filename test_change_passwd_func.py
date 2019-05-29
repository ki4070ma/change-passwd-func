#!/usr/bin/env python

import pytest

from change_passwd_func import change_passwd_func

OLD_PASSWD = 'OLD'

VALID_BASE_PASSWD_LEN4 = '1aB!'
MIN_VALID_LENGTH = 18

@pytest.mark.parametrize('length', [0, 3, 17])
def test_change_passwd_func_less_length_0(length):
    assert not change_passwd_func(OLD_PASSWD, 'a'*length)
    # assert change_passwd_func(OLD_PASSWD, new_passwd)

@pytest.mark.parametrize('length', [18, 19])
def test_change_passwd_func_enough_length_18(length):
    new_passwd = str_padding(VALID_BASE_PASSWD_LEN4, length)
    assert change_passwd_func(OLD_PASSWD, new_passwd)

@pytest.mark.parametrize('invalid_char', ['-'])
def test_change_passwd_func_invalid_char(invalid_char):
    new_passwd = str_padding(invalid_char)
    assert not change_passwd_func(OLD_PASSWD, new_passwd)

@pytest.mark.parametrize('special_char', ['!', '@', '#', '$', '&', '*'])
def test_change_passwd_func_valid_special_char(special_char):
    new_passwd = str_padding(special_char)
    assert change_passwd_func(OLD_PASSWD, new_passwd)

@pytest.mark.parametrize('continous_num', [3])
def test_change_password_func_continuous_3_num(continous_num):
    new_passwd = str_padding('a'*continous_num)
    assert change_passwd_func(OLD_PASSWD, new_passwd)

@pytest.mark.parametrize('continous_num', [4, 5])
def test_change_password_func_continuous_3_num(continous_num):
    new_passwd = str_padding('a'*continous_num)
    assert not change_passwd_func(OLD_PASSWD, new_passwd)


def str_padding(string, length=MIN_VALID_LENGTH, padding_src_str=VALID_BASE_PASSWD_LEN4):
    l = len(padding_src_str)
    for i in range(length):
        string += padding_src_str[i % l]
    return string