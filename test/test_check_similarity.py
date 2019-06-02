#!/usr/bin/env python

import pytest

from change_passwd_func.check_similarity import check_similarity
from change_passwd_func.constants import SIMILARITY_THRESHOLD


class TestCheckSimilarity(object):

    class TestCheckSimilaritySameStringLength(object):

        LENGTH = 100

        @pytest.mark.parametrize('str_diff_num', [-1, 0])  # 79%/80% matching
        def test_check_passwd_not_similar(self, str_diff_num):
            assert not self._test_check_passwd(str_diff_num)

        @pytest.mark.parametrize('str_diff_num', [1])  # 81% matching
        def test_check_passwd_similar(self, str_diff_num):
            assert self._test_check_passwd(str_diff_num)

        def _test_check_passwd(self, str_diff_num):
            len1 = int(self.LENGTH * SIMILARITY_THRESHOLD + str_diff_num)
            str1 = '{}{}'.format('a' * len1, 'b' * (self.LENGTH - len1))
            str2 = 'a'*self.LENGTH
            return check_similarity(str1, str2)


    class TestCheckSimilarityDifferentStringLength(object):

        LENGTH = 100

        def test_check_passwd_not_similar_new_pswd_longer(self):  # 79% matching
            str1 = 'a'*int(self.LENGTH * SIMILARITY_THRESHOLD - 1)
            str2 = 'a'*self.LENGTH
            assert not check_similarity(str1, str2)

        def test_check_passwd_not_similar_new_pswd_longer_on_SIMILARITY_THRESHOLD(self):  # 80% matching
            str1 = 'a'*int(self.LENGTH * SIMILARITY_THRESHOLD)
            str2 = 'a'*self.LENGTH
            assert not check_similarity(str1, str2)

        def test_check_passwd_similar_new_pswd_longer(self):  # 81% matching
            str1 = 'a'*int(self.LENGTH * SIMILARITY_THRESHOLD + 1)
            str2 = 'a'*self.LENGTH
            assert check_similarity(str1, str2)

        def test_check_passwd_not_similar_old_pswd_longer(self):  # 79% matching
            str1 = 'a'*self.LENGTH
            str2 = 'a'*int(self.LENGTH * SIMILARITY_THRESHOLD - 1)
            assert not check_similarity(str1, str2)

        def test_check_passwd_not_similar_old_pswd_longer_on_SIMILARITY_THRESHOLD(self):  # 80% matching
            str1 = 'a'*self.LENGTH
            str2 = 'a'*int(self.LENGTH * SIMILARITY_THRESHOLD)
            assert not check_similarity(str1, str2)

        def test_check_passwd_similar_old_pswd_longer(self):  # 81% matching
            str1 = 'a'*self.LENGTH
            str2 = 'a'*int(self.LENGTH * SIMILARITY_THRESHOLD + 1)
            assert check_similarity(str1, str2)
