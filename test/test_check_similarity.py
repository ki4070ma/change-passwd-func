#!/usr/bin/env python

import pytest

from change_passwd_func.check_similarity import check_similarity
from change_passwd_func.constants import SIMILARITY_THRESHOLD


class TestCheckSimilarity(object):

    class TestCheckSimilaritySameTailString(object):

        LENGTH = 100

        # TestIdx: 1, 2
        @pytest.mark.parametrize('str_diff_num', [-1, 0])  # 79%/80% matching
        def test_check_similarity_not_similar(self, str_diff_num):
            assert not self._check_similarity_same_tail(str_diff_num)

        # TestIdx: 3
        @pytest.mark.parametrize('str_diff_num', [1])  # 81% matching
        def test_check_similarity_similar(self, str_diff_num):
            assert self._check_similarity_same_tail(str_diff_num)

        def _check_similarity_same_tail(self, str_diff_num):
            '''Check similarity between two strings with `str_diff_num`.

            One string has difference which is timed by `SIMILARITY_THRESHOLD`
            and added `str_diff_num`.
            Two strings has the same strings at TAIL.

            Example:
                `SIMILARITY_THRESHOLD` is 0.8.
                Below strings will be compared with `LENGTH`:10, `str_diff_num`: 1
                    str1: XXXooooooo
                    str2: oooooooooo
                Below strings will be compared with `LENGTH`:10, `str_diff_num`: 0
                    str1: XXoooooooo
                    str2: oooooooooo
                Below strings will be compared with `LENGTH`:10, `str_diff_num`: -1
                    str1: Xooooooooo
                    str2: oooooooooo

            Args:
                str_diff_num(int): additional the number of string difference

            Returns:
                bool: `check_similarity` result
            '''

            len1 = int(self.LENGTH * SIMILARITY_THRESHOLD + str_diff_num)
            str1 = '{}{}'.format('X'*(self.LENGTH - len1), 'o'*len1)
            str2 = 'o'*self.LENGTH
            return check_similarity(str1, str2)

    class TestCheckSimilaritySameCenterString(object):

        LENGTH = 100

        # TestIdx: 4, 5
        @pytest.mark.parametrize('str_diff_num', [-1, 0])  # 79%/80% matching
        def test_check_similarity_not_similar(self, str_diff_num):
            assert not self._check_similarity_same_center(str_diff_num)

        # TestIdx: 6
        @pytest.mark.parametrize('str_diff_num', [1])  # 81% matching
        def test_check_similarity_similar(self, str_diff_num):
            assert self._check_similarity_same_center(str_diff_num)

        def _check_similarity_same_center(self, str_diff_num):
            '''Check similarity between two strings with `str_diff_num`.

            One string has difference which is timed by `SIMILARITY_THRESHOLD`
            and added `str_diff_num`.
            Two strings has the same strings at CENTER.

            Example:
                `SIMILARITY_THRESHOLD` is 0.8.
                Below strings will be compared with `LENGTH`:10, `str_diff_num`: 1
                    str1: ooooXXXooo
                    str2: oooooooooo
                Below strings will be compared with `LENGTH`:10, `str_diff_num`: 0
                    str1: ooooXXoooo
                    str2: oooooooooo
                Below strings will be compared with `LENGTH`:10, `str_diff_num`: -1
                    str1: ooooXooooo
                    str2: oooooooooo

            Args:
                str_diff_num(int): additional the number of string difference

            Returns:
                bool: `check_similarity` result
            '''

            len1 = int(self.LENGTH * SIMILARITY_THRESHOLD + str_diff_num)
            str1 = '{}{}{}'.format('o'*int(len1 / 2), 'X'*(self.LENGTH - len1), 'o'*(len1 - int(len1 / 2)))
            str2 = 'o'*self.LENGTH
            return check_similarity(str1, str2)


    class TestCheckSimilaritySameHeadStringLength(object):

        LENGTH = 100

        # TestIdx: 7, 8
        @pytest.mark.parametrize('str_diff_num', [-1, 0])  # 79%/80% matching
        def test_check_similarity_not_similar(self, str_diff_num):
            assert not self._check_similarity_same_head(str_diff_num)

        # TestIdx: 9
        @pytest.mark.parametrize('str_diff_num', [1])  # 81% matching
        def test_check_similarity_similar(self, str_diff_num):
            assert self._check_similarity_same_head(str_diff_num)

        def _check_similarity_same_head(self, str_diff_num):
            '''Check similarity between two strings with `str_diff_num`.

            One string has difference which is timed by `SIMILARITY_THRESHOLD`
            and added `str_diff_num`.
            Two strings has the same strings at HEAD.

            Example:
                `SIMILARITY_THRESHOLD` is 0.8.
                Below strings will be compared with `LENGTH`:10, `str_diff_num`: 1
                    str1: oooooooXXX
                    str2: oooooooooo
                Below strings will be compared with `LENGTH`:10, `str_diff_num`: 0
                    str1: ooooooooXX
                    str2: oooooooooo
                Below strings will be compared with `LENGTH`:10, `str_diff_num`: -1
                    str1: oooooooooX
                    str2: oooooooooo

            Args:
                str_diff_num(int): additional the number of string difference

            Returns:
                bool: `check_similarity` result
            '''

            len1 = int(self.LENGTH * SIMILARITY_THRESHOLD + str_diff_num)
            str1 = '{}{}'.format('o'*len1, 'X'*(self.LENGTH - len1))
            str2 = 'o'*self.LENGTH
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
