#!/usr/bin/env python

SP_CHARS = ['!', '@', '#', '$', '&', '*']

OLD_PASSWD = 'OLD'

VALID_BASE_PASSWD_LEN4 = '1aB2'

MIN_VALID_LENGTH = 18


def passwd_padding(string='', length=MIN_VALID_LENGTH, padding_src_str=VALID_BASE_PASSWD_LEN4, include_sp_char=True):
    l = len(padding_src_str)
    for i in range(length):
        string += padding_src_str[i % l]
    if include_sp_char:
        string = string[:-1] + SP_CHARS[0]
    return string
