#!/usr/bin/env python

from change_passwd_func.check_similarity import check_similarity


class TestCheckSimilarity(object):

    def test_check_passwd_not_similar_79_percent(self):
        str1 = '{}{}'.format('a'*79, 'b'*21)
        str2 = 'a'*100
        assert not check_similarity(str1, str2)

    def test_check_passwd_not_similar_80_percent(self):
        str1 = '{}{}'.format('a'*80, 'b'*20)
        str2 = 'a'*100
        assert not check_similarity(str1, str2)

    def test_check_passwd_not_similar_81_percent(self):
        str1 = '{}{}'.format('a'*81, 'b'*19)
        str2 = 'a'*100
        assert check_similarity(str1, str2)
