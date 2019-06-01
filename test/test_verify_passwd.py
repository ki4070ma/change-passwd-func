#!/usr/bin/env python

from test.helper.helper import create_passwd

import pytest

from change_passwd_func.constants import (
    MAX_CHAR_CONTINUOUS_NUM,
    MAX_SP_CHAR_NUM,
    MIN_VALID_LENGTH,
    SP_CHARS
)
from change_passwd_func.verify_passwd import verify_passwd


class TestVerifyPasswd(object):

    class TestVerifyPasswdLength(object):
        @pytest.mark.parametrize('length', [0, MIN_VALID_LENGTH-1])
        def test_verify_passwd_not_enough_length(self, length):
            assert not verify_passwd(create_passwd(length=length))

        @pytest.mark.parametrize('length', [MIN_VALID_LENGTH, MIN_VALID_LENGTH+1, 1000])
        def test_verify_passwd_valid_length_18(self, length):
            assert verify_passwd(create_passwd(length=length))

    class TestVerifyPasswdInvalidChar(object):
        @pytest.mark.parametrize('invalid_char', ['-'])
        def test_verify_passwd_invalid_char(self, invalid_char):
            assert not verify_passwd(create_passwd(incl_str=invalid_char))

    class TestVerifyPasswdSpecialChar(object):
        @pytest.mark.parametrize('special_char', SP_CHARS)
        def test_verify_passwd_valid_special_char(self, special_char):
            assert verify_passwd(create_passwd(incl_str=special_char))

    class TestVerifyPassowdContinuousSameChar(object):
        @pytest.mark.parametrize('continous_num', [MAX_CHAR_CONTINUOUS_NUM-1, MAX_CHAR_CONTINUOUS_NUM])
        def test_verify_passwd_valid_continuous_same_char_num(self, continous_num):
            assert verify_passwd(create_passwd(incl_str='a'*continous_num))

        @pytest.mark.parametrize('continous_num', [MAX_CHAR_CONTINUOUS_NUM+1])
        def test_verify_passwd_over_continuous_same_char_num(self, continous_num):
            assert not verify_passwd(create_passwd('a'*continous_num))

    class TestVerifyPasswdSpecialCharNum(object):
        @pytest.mark.parametrize('sp_char_num', [MAX_SP_CHAR_NUM-1, MAX_SP_CHAR_NUM])
        def test_verify_passwd_valid_sp_char_num(self, sp_char_num):
            sp_chars = create_passwd(length=sp_char_num, padding_src_str=SP_CHARS, incl_sp_char=False)
            assert verify_passwd(create_passwd(incl_str=sp_chars, incl_sp_char=False))

        @pytest.mark.parametrize('sp_char_num', [MAX_SP_CHAR_NUM+1])
        def test_verify_passwd_over_sp_char_num(self, sp_char_num):
            sp_chars = create_passwd(length=sp_char_num, padding_src_str=SP_CHARS, incl_sp_char=False)
            assert not verify_passwd(create_passwd(incl_str=sp_chars, incl_sp_char=False))

    class TestVerifyPasswdNumericLimitation(object):
        @pytest.mark.parametrize('length', [20])  # [even] num:10, alphabet:9, sp:1  # TODO hard to understand
        def test_verify_passwd_num_more_than_half_of_length_even(self, length):
            assert verify_passwd(create_passwd(incl_str='!1', length=length, incl_sp_char=False))

        @pytest.mark.parametrize('length', [21])  # [odd] num:10, alphabet:10, sp:1  # TODO hard to understand
        def test_verify_passwd_num_more_than_half_of_length_odd(self, length):
            assert verify_passwd(create_passwd(incl_str='!1', length=length, incl_sp_char=False))

        @pytest.mark.parametrize('length', [20])  # [even] num:11, alphabet:8, sp:1  # TODO hard to understand
        def test_verify_passwd_num_less_than_half_of_length(self, length):
            assert not verify_passwd(create_passwd(incl_str='!12', length=length, incl_sp_char=False))

        @pytest.mark.parametrize('length', [21])  # [odd] num:11, alphabet:9, sp:1  # TODO hard to understand
        def test_verify_passwd_num_less_than_half_of_length(self, length):
            assert not verify_passwd(create_passwd(incl_str='!12', length=length, incl_sp_char=False))
