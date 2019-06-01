#!/usr/bin/env python

from change_passwd_func.check_similarity import check_similarity

class TestCheckSimilarity(object):

    def test_check_passwd_not_similar_90_percent(self):
        str1 = 'abcdefghij'
        str2 = 'abcdefghi1'
        assert check_similarity(str1, str2)

    def test_check_passwd_not_similar_80_percent(self):
        str1 = 'abcdefghif'
        str2 = 'abcdefgh12'
        assert not check_similarity(str1, str2)

    def test_check_passwd_not_similar_70_percent(self):
        str1 = 'abcdefghij'
        str2 = 'abcdefg123'
        assert not check_similarity(str1, str2)

