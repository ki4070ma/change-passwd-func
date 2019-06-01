#!/usr/bin/env python

from change_passwd_func.check_similarity import check_similarity
from change_passwd_func.constants import SIMILARITY_THRESHOLD


class TestCheckSimilarity(object):

    class TestCheckSimilaritySamePassLength(object):

        length = 100

        def test_check_passwd_not_similar_79_percent(self):
            str1 = '{}{}'.format('a'*(self.length*SIMILARITY_THRESHOLD-1),
                                 'b'*(self.length*(1-SIMILARITY_THRESHOLD)+1))
            str2 = 'a'*self.length
            assert not check_similarity(str1, str2)

        def test_check_passwd_not_similar_80_percent(self):
            str1 = '{}{}'.format('a'*(self.length*SIMILARITY_THRESHOLD),
                                 'b'*(self.length*(1-SIMILARITY_THRESHOLD)))
            str2 = 'a'*self.length
            assert not check_similarity(str1, str2)

        def test_check_passwd_not_similar_81_percent(self):
            str1 = '{}{}'.format('a'*(self.length*SIMILARITY_THRESHOLD+1),
                                 'b'*(self.length*(1-SIMILARITY_THRESHOLD)-1))
            str2 = 'a'*self.length
            assert check_similarity(str1, str2)
