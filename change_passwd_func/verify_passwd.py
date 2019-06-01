#!/usr/bin/env python

from change_passwd_func.constants import (
    MAX_CHAR_CONTINUOUS_NUM,
    MAX_SP_CHAR_NUM,
    MIN_VALID_LENGTH,
    SP_CHARS
)


def verify_passwd(passwd):
    print(passwd)
    if len(passwd) < MIN_VALID_LENGTH:
        print('not enough length')
        return False
    elif _include_invalid_char(passwd):
        print('included invalid char')
        return False
    elif _include_not_all_patterns(passwd):
        print("didn't include all necessary patterns")
        return False
    elif _include_over_continuous_same_chars(passwd):
        print('included continous more thna {} same chars'.format(MAX_CHAR_CONTINUOUS_NUM))
        return False
    elif _include_over_sp_char_num(passwd):
        print('included more than {} special characters'.format(MAX_SP_CHAR_NUM))
        return False
    elif _include_num_more_than_half_of_length(passwd):
        print('50 % of password should not be a number')
        return False
    return True


def _include_invalid_char(passwd):
    for x in passwd:
        if not x.isalnum() and x not in SP_CHARS:
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
    return count > len(passwd) / 2.0


if __name__ == '__main__':
    pass
