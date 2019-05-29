#!/usr/bin/env python

from helper.helper import SP_CHARS

def verify_passwd(passwd):
    if len(passwd) < 18:
        print('not enough length')
        return False
    if len([False for x in passwd if not x.isalnum() and x not in SP_CHARS]) > 0:
        print('included invalid char')
        return False
    if not _include_all_patterns(passwd):
        print("didn't include all pattern")
        return False
    if _include_continuous_4_same_chars(passwd):
        print('included continous 4 same chars')
        return False
    return True

def _include_all_patterns(passwd):
    upper_flg = False
    lower_flg = False
    num_flg = False
    special_flg = False
    for x in passwd:
        if x.isupper():
            upper_flg = True
        elif x.islower():
            lower_flg = True
        elif x.isnumeric():
            num_flg = True
        elif x in SP_CHARS:
            special_flg = True
    return upper_flg and lower_flg and num_flg and special_flg

def _include_continuous_4_same_chars(passwd):
    count = 1
    prev_char = passwd[0]
    for x in list(passwd)[1:]:
        if x == prev_char:
            count += 1
        else:
            count = 1
            prev_char = x
        if count > 3:
            return True
    return False
