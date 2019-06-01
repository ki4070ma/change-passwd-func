#!/usr/bin/env python

from Levenshtein import distance

from .constants import SIMILARITY_THRESHOLD


def check_similarity(string1, string2):
    normalized_distance = distance(string1, string2) / max(len(string1), len(string2))
    print('similarity: {}%'.format(int((1-normalized_distance)*100)))
    return normalized_distance < 1 - SIMILARITY_THRESHOLD


if __name__ == '__main__':
    str1 = 'abcdefghijf'
    str2 = 'abcdefghi12'
    print('str1: {}'.format(str1))
    print('str2: {}'.format(str2))
    print(check_similarity(str1, str2))

    str1 = 'abcdefghijf'
    str2 = 'abcdefgh123'
    print('str1: {}'.format(str1))
    print('str2: {}'.format(str2))
    print(check_similarity(str1, str2))
