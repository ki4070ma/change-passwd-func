#!/usr/bin/env python

import pytest

from change_passwd_func.check_similarity import check_similarity
from change_passwd_func.constants import SIMILARITY_THRESHOLD


class TestCheckSimilarity(object):

    class TestCheckSimilaritySameStringLength(object):

        LENGTH = 100

        @pytest.mark.parametrize('str_diff_num', [-1, 0])  # 79%/80% matching
        def test_check_similarity_not_similar_src_dist_same_length(self, str_diff_num):
            assert not self._check_similarity(str_diff_num)

        @pytest.mark.parametrize('str_diff_num', [1])  # 81% matching
        def test_check_similarity_similar_src_dist_same_length(self, str_diff_num):
            assert self._check_similarity(str_diff_num)

        def _check_similarity(self, str_diff_num):
            len1 = int(self.LENGTH * SIMILARITY_THRESHOLD + str_diff_num)
            str1 = '{}{}'.format('a'*len1, 'b'*(self.LENGTH - len1))
            str2 = 'a'*self.LENGTH
            return check_similarity(str1, str2)

    class TestCheckSimilarityDifferentStringLength(object):

        LENGTH = 100

        @pytest.mark.parametrize('str_diff_num', [-1, 0])
        def test_check_similarity_not_similar_dist_string_longer(self, str_diff_num):  # 79%/80% matching
            assert not self._check_similarity_dist_psswd_longer(str_diff_num)

        @pytest.mark.parametrize('str_diff_num', [1])
        def test_check_similarity_similar_dist_string_longer(self, str_diff_num):  # 81% matching
            assert self._check_similarity_dist_psswd_longer(str_diff_num)

        def _check_similarity_dist_psswd_longer(self, str_diff_num):
            len1 = int(self.LENGTH*SIMILARITY_THRESHOLD + str_diff_num)
            len2 = self.LENGTH
            return self._check_similarity(len1, len2)

        @pytest.mark.parametrize('str_diff_num', [-1, 0])
        def test_check_similarity_not_similar_src_string_longer(self, str_diff_num):  # 79%/80% matching
            assert not self._check_similarity_src_string_longer(str_diff_num)

        @pytest.mark.parametrize('str_diff_num', [1])
        def test_check_similarity_similar_src_string_longer(self, str_diff_num):  # 81% matching
            assert self._check_similarity_src_string_longer(str_diff_num)

        def _check_similarity_src_string_longer(self, str_diff_num):
            len1 = self.LENGTH
            len2 = int(self.LENGTH*SIMILARITY_THRESHOLD + str_diff_num)
            return self._check_similarity(len1, len2)

        def _check_similarity(self, len1, len2):
            return check_similarity('a'*len1, 'a'*len2)
