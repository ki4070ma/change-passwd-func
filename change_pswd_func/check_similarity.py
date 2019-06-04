#!/usr/bin/env python

from Levenshtein import distance

from .constants import SIMILARITY_THRESHOLD


def similar(string1, string2):
    '''

    Considered that strings1/2 has alphabet or numeric or special chars(`constants.SP_CHARS`)

    [Change password requirement]
    3. password is not similar to old password < 80% match.

    '''

    print('\n[string1]: {}'.format(string1))
    print('[string2]: {}'.format(string2))
    normalized_distance = distance(string1, string2) / max(len(string1), len(string2))
    print('[similarity]: {}%'.format(int((1-normalized_distance)*100)))
    return 1 - normalized_distance > SIMILARITY_THRESHOLD
