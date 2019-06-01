#!/usr/bin/env python

from test.helper.helper import pswd_generator

import pytest

from change_passwd_func.constants import (
    MAX_CHAR_CONTINUOUS_NUM,
    MAX_SP_CHAR_NUM,
    MAX_VALID_LENGTH,
    MIN_VALID_LENGTH,
    SP_CHARS
)
from change_passwd_func.verify_passwd import verify_passwd


class TestVerifyPasswd(object):

    class TestVerifyPasswdLength(object):
        # TestIdx: 1
        @pytest.mark.parametrize('length', [0])
        def test_verify_passwd_not_enough_length_0(self, length):
            assert not verify_passwd(pswd_generator(length=length, incl_sp_char=False))

        # TestIdx: 2
        @pytest.mark.parametrize('length', [MIN_VALID_LENGTH-1, MAX_VALID_LENGTH+1])
        def test_verify_passwd_not_enough_length(self, length):
            assert not verify_passwd(pswd_generator(length=length))

        # TestIdx: 3, 4
        @pytest.mark.parametrize('length', [MIN_VALID_LENGTH, MIN_VALID_LENGTH+1, MAX_VALID_LENGTH])
        def test_verify_passwd_valid_length_18(self, length):
            assert verify_passwd(pswd_generator(length=length))

    class TestVerifyPasswdInvalidChar(object):
        # TestIdx: 5
        def test_verify_passwd_invalid_char(self):
            assert not verify_passwd(pswd_generator(incl_invalid_char=True))

        @pytest.mark.parametrize('invalid_char', ['あ', '^', '朝', 'ไทย', 'Ａ'])
        def test_verify_passwd_various_invalid_char(self, invalid_char):
            assert not verify_passwd(pswd_generator(pswd_base=invalid_char))

    class TestVerifyPasswdSpecialChar(object):
        # TestIdx: 6
        def test_verify_passwd_non_valid_special_char(self):
            assert not verify_passwd(pswd_generator(incl_sp_char=False))

    class TestVerifyPassowdContinuousSameChar(object):
        # TestIdx: 10, 11
        @pytest.mark.parametrize('continous_num', [MAX_CHAR_CONTINUOUS_NUM-1, MAX_CHAR_CONTINUOUS_NUM])
        def test_verify_passwd_valid_continuous_same_char_num(self, continous_num):
            assert verify_passwd(pswd_generator(pswd_base='a' * continous_num))

        # TestIdx: 12
        @pytest.mark.parametrize('continous_num', [MAX_CHAR_CONTINUOUS_NUM+1])
        def test_verify_passwd_over_continuous_same_char_num(self, continous_num):
            assert not verify_passwd(pswd_generator(pswd_base='a' * continous_num))

    class TestVerifyPasswdNumericLimitation(object):
        # TODO Hard to understand how password generated for these cases

        # TestIdx: 14
        @pytest.mark.parametrize('length', [21])  # [odd] num:10, alphabet:10, sp:1
        def test_verify_passwd_num_less_than_half_of_length_odd(self, length):
            assert verify_passwd(pswd_generator(pswd_base='!12', length=length, incl_sp_char=False))

        # TestIdx: 15
        @pytest.mark.parametrize('length', [21])  # [odd] num:11, alphabet:9, sp:1
        def test_verify_passwd_num_more_than_half_of_length_odd(self, length):
            assert not verify_passwd(pswd_generator(pswd_base='!123', length=length, incl_sp_char=False))

        # TestIdx: 16
        @pytest.mark.parametrize('length', [20])  # [even] num:9, alphabet:10, sp:1
        def test_verify_passwd_num_less_than_half_of_length_even(self, length):
            assert verify_passwd(pswd_generator(pswd_base='!1', length=length, incl_sp_char=False))
        # TestIdx: 17
        @pytest.mark.parametrize('length', [20])  # [even] num:10, alphabet:9, sp:1
        def test_verify_passwd_num_half_of_length(self, length):
            assert not verify_passwd(pswd_generator(pswd_base='!12', length=length, incl_sp_char=False))

        # TestIdx: 18
        @pytest.mark.parametrize('length', [20])  # [even] num:11, alphabet:8, sp:1
        def test_verify_passwd_num_more_than_half_of_length_even(self, length):
            assert not verify_passwd(pswd_generator(pswd_base='!123', length=length, incl_sp_char=False))

    class TestVerifyPasswdSpecialCharNum(object):
        # TestIdx: 19, 20
        @pytest.mark.parametrize('sp_char_num', [MAX_SP_CHAR_NUM-1, MAX_SP_CHAR_NUM])
        def test_verify_passwd_valid_sp_char_num(self, sp_char_num):
            pswd = ''.join([SP_CHARS[i % len(SP_CHARS)] for i in range(sp_char_num)])
            assert verify_passwd(pswd_generator(pswd_base=pswd, incl_sp_char=False))

        # TestIdx: 21
        @pytest.mark.parametrize('sp_char_num', [MAX_SP_CHAR_NUM+1])
        def test_verify_passwd_over_sp_char_num(self, sp_char_num):
            pswd = ''.join([SP_CHARS[i % len(SP_CHARS)] for i in range(sp_char_num)])
            assert not verify_passwd(pswd_generator(pswd_base=pswd, incl_sp_char=False))
