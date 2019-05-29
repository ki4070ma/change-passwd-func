#!/usr/bin/env python

SP_CHARS = ['!', '@', '#', '$', '&', '*']

OLD_PASSWD = 'OLD'

VALID_BASE_PASSWD_LEN4 = '1aB!'

MIN_VALID_LENGTH = 18


def passwd_padding(string='', length=MIN_VALID_LENGTH, padding_src_str=VALID_BASE_PASSWD_LEN4):
    l = len(padding_src_str)
    for i in range(length):
        string += padding_src_str[i % l]
    return string
