#!/usr/bin/env python

import re

from .constants import (
    MAX_CHAR_CONTINUOUS_NUM,
    MAX_SP_CHAR_NUM,
    MAX_VALID_LENGTH,
    MIN_VALID_LENGTH,
    SP_CHARS
)
from .error_msg import ErrorMsgVerifyPswd


def verify_passwd(passwd):
    print('\n[passwd]: {}'.format(passwd))
    if len(passwd) < MIN_VALID_LENGTH or len(passwd) > MAX_VALID_LENGTH:
        print('Password length is {}.'.format(len(passwd)))
        print(ErrorMsgVerifyPswd.INVALID_LENGTH)
    elif _include_invalid_char(passwd):
        print(ErrorMsgVerifyPswd.INVALID_CHAR)
    elif _include_not_all_patterns(passwd):
        print(ErrorMsgVerifyPswd.NOT_ALL_PATTERNS)
    elif _include_over_continuous_same_chars(passwd):
        print(ErrorMsgVerifyPswd.OVER_CONTINUOUS_SAME_CHARS)
    elif _include_over_sp_char_num(passwd):
        print(ErrorMsgVerifyPswd.OVER_SP_CHAR_NUM)
    elif _include_num_more_than_half_of_length(passwd):
        print(ErrorMsgVerifyPswd.MORE_THAN_HALF_OF_LENGTH)
    else:
        print('Valid passwd')
        return True
    return False


def _include_invalid_char(passwd):
    for x in passwd:
        if not bool(re.search('[0-9a-zA-Z]', x)) and x not in SP_CHARS:  # x.isalnum() unavailable for Hiragana, Kanji, etc
            return True
    return False


def _include_not_all_patterns(passwd):
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
        if upper_flg and lower_flg and num_flg and special_flg:
            return False
    return True


def _include_over_continuous_same_chars(passwd):
    count = 1
    prev_char = passwd[0]
    for x in list(passwd)[1:]:
        if x == prev_char:
            count += 1
        else:
            # Reset
            count = 1
            prev_char = x
        if count > MAX_CHAR_CONTINUOUS_NUM:
            return True
    return False


def _include_over_sp_char_num(passwd):
    count = 0
    for c in SP_CHARS:
        count += passwd.count(c)
    return count > MAX_SP_CHAR_NUM


def _include_num_more_than_half_of_length(passwd):
    count = 0
    for c in passwd:
        if c.isnumeric():
            count += 1
    return count >= len(passwd) / 2.0
