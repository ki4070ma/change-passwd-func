#!/usr/bin/env python

SP_CHARS = ['!', '@', '#', '$', '&', '*']

VALID_PASSWD_BASE = '1aB2'

MIN_VALID_LENGTH = 18


def create_passwd(incl_str='', length=MIN_VALID_LENGTH, padding_src_str=VALID_PASSWD_BASE, incl_sp_char=True):
    l = len(padding_src_str)
    for i in range(length):
        incl_str += padding_src_str[i % l]
    if incl_sp_char:
        incl_str = incl_str[:-1] + SP_CHARS[0]
    return incl_str
