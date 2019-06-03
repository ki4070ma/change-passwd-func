#!/usr/bin/env python

import pytest

from change_pswd_func.change_pswd_func import change_pswd_func
from test.helper.helper import pswd_changer, pswd_generator

from change_pswd_func.constants import (
    MAX_VALID_LENGTH,
    MIN_VALID_LENGTH,
    SIMILARITY_THRESHOLD
)


class TestChangePasswd(object):

    @pytest.mark.parametrize('length', [0])
    def test_change_pswd_not_enough_length_0(self, length):
        old_pswd = pswd_generator(length=length, incl_sp_char=False)
        new_pswd = 'DUMMY'
        assert not change_pswd_func(old_pswd, new_pswd)

    @pytest.mark.parametrize('length',[MIN_VALID_LENGTH, MIN_VALID_LENGTH + 1, MAX_VALID_LENGTH])
    @pytest.mark.parametrize('add_diff_ratio', [0, -0.01])  # 79%/80% matching
    def test_verify_pswd_valid_length_dissimilar(self, length, add_diff_ratio):
        old_pswd = pswd_generator(length=length)
        new_pswd = pswd_changer(old_pswd, diff_ratio=(1-SIMILARITY_THRESHOLD+add_diff_ratio))
        assert change_pswd_func(old_pswd, new_pswd)

    @pytest.mark.parametrize('length',[100, MAX_VALID_LENGTH])
    @pytest.mark.parametrize('add_diff_ratio', [0.01])  # 81% matching
    def test_verify_pswd_valid_length_similar(self, length, add_diff_ratio):
        old_pswd = pswd_generator(length=length)
        new_pswd = pswd_changer(old_pswd, diff_ratio=(1-SIMILARITY_THRESHOLD+add_diff_ratio))
        assert not change_pswd_func(old_pswd, new_pswd)
