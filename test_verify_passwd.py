#!/usr/bin/env python

import pytest

from helper.helper import passwd_padding, SP_CHARS
from verify_passwd import verify_passwd


@pytest.mark.parametrize('length', [0, 16, 17])
def test_change_passwd_func_less_length(length):
    assert not verify_passwd(passwd_padding(length=length))

@pytest.mark.parametrize('length', [18, 19, 1000])
def test_change_passwd_func_enough_length_18(length):
    assert verify_passwd(passwd_padding(length=length))

@pytest.mark.parametrize('invalid_char', ['-'])
def test_change_passwd_func_invalid_char(invalid_char):
    assert not verify_passwd(passwd_padding(string=invalid_char))

@pytest.mark.parametrize('special_char', ['!', '@', '#', '$', '&', '*'])
def test_change_passwd_func_valid_special_char(special_char):
    assert verify_passwd(passwd_padding(string=special_char))

@pytest.mark.parametrize('continous_num', [3, 4])
def test_change_passwd_func_continuous_3(continous_num):
    assert verify_passwd(passwd_padding(string='a'*continous_num))

@pytest.mark.parametrize('continous_num', [5, 6])
def test_change_passwd_func_continuous_more_than_3(continous_num):
    assert not verify_passwd(passwd_padding('a'*continous_num))

@pytest.mark.parametrize('sp_char_num', [3, 4])
def test_change_passwd_func_less_than_5_sp_char(sp_char_num):
    sp_chars = passwd_padding(length=sp_char_num, padding_src_str=SP_CHARS, include_sp_char=False)
    assert verify_passwd(passwd_padding(string=sp_chars, include_sp_char=False))

@pytest.mark.parametrize('sp_char_num', [5, 6])
def test_change_passwd_func_more_than_4_sp_char(sp_char_num):
    sp_chars = passwd_padding(length=sp_char_num, padding_src_str=SP_CHARS, include_sp_char=False)
    assert not verify_passwd(passwd_padding(string=sp_chars, include_sp_char=False))
