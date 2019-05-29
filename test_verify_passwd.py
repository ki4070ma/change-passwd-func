#!/usr/bin/env python

import pytest

from helper.helper import create_passwd, SP_CHARS, VALID_BASE_PASSWD_LEN4
from verify_passwd import verify_passwd


@pytest.mark.parametrize('length', [0, 16, 17])
def test_verify_passwd_less_length(length):
    assert not verify_passwd(create_passwd(length=length))

@pytest.mark.parametrize('length', [18, 19, 1000])
def test_verify_passwd_enough_length_18(length):
    assert verify_passwd(create_passwd(length=length))

@pytest.mark.parametrize('invalid_char', ['-'])
def test_verify_passwd_invalid_char(invalid_char):
    assert not verify_passwd(create_passwd(string=invalid_char))

@pytest.mark.parametrize('special_char', ['!', '@', '#', '$', '&', '*'])
def test_verify_passwd_valid_special_char(special_char):
    assert verify_passwd(create_passwd(string=special_char))

@pytest.mark.parametrize('continous_num', [3, 4])
def test_verify_passwd_continuous_3(continous_num):
    assert verify_passwd(create_passwd(string='a' * continous_num))

@pytest.mark.parametrize('continous_num', [5, 6])
def test_verify_passwd_continuous_more_than_3(continous_num):
    assert not verify_passwd(create_passwd('a' * continous_num))

@pytest.mark.parametrize('sp_char_num', [3, 4])
def test_verify_passwd_less_than_5_sp_char(sp_char_num):
    sp_chars = create_passwd(length=sp_char_num, padding_src_str=SP_CHARS, include_sp_char=False)
    assert verify_passwd(create_passwd(string=sp_chars, include_sp_char=False))

@pytest.mark.parametrize('sp_char_num', [5, 6])
def test_verify_passwd_more_than_4_sp_char(sp_char_num):
    sp_chars = create_passwd(length=sp_char_num, padding_src_str=SP_CHARS, include_sp_char=False)
    assert not verify_passwd(create_passwd(string=sp_chars, include_sp_char=False))

@pytest.mark.parametrize('length', [20, 21])  # even, odd
def test_verify_passwd_num_more_than_half_of_length(length):
    # VALID_BASE_PASSWD_LEN4 -> num : non num = 1 : 1
    assert verify_passwd(create_passwd(string='1', length=length, padding_src_str=VALID_BASE_PASSWD_LEN4))
