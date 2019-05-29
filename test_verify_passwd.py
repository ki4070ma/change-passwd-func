#!/usr/bin/env python

import pytest

from helper.helper import passwd_padding
from verify_passwd import verify_passwd


@pytest.mark.parametrize('length', [0, 3, 17])
def test_change_passwd_func_less_length(length):
    assert not verify_passwd(passwd_padding(length=length))

@pytest.mark.parametrize('length', [18, 19])
def test_change_passwd_func_enough_length_18(length):
    assert verify_passwd(passwd_padding(length=length))

@pytest.mark.parametrize('invalid_char', ['-'])
def test_change_passwd_func_invalid_char(invalid_char):
    assert not verify_passwd(passwd_padding(string=invalid_char))

@pytest.mark.parametrize('special_char', ['!', '@', '#', '$', '&', '*'])
def test_change_passwd_func_valid_special_char(special_char):
    assert verify_passwd(passwd_padding(string=special_char))

@pytest.mark.parametrize('continous_num', [3])
def test_change_password_func_continuous_3(continous_num):
    assert verify_passwd(passwd_padding(string='a'*continous_num))

@pytest.mark.parametrize('continous_num', [4, 5])
def test_change_password_func_continuous_more_than_3(continous_num):
    assert not verify_passwd(passwd_padding('a'*continous_num))
