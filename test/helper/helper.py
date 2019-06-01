#!/usr/bin/env python

from change_passwd_func.constants import MIN_VALID_LENGTH, SP_CHARS

VALID_PASSWD_BASE = '1aB2'

INVALID_CHAR = '-'


def pswd_generator(
        password='',
        length=MIN_VALID_LENGTH,
        incl_invalid_char=False,
        incl_upper_char=True,
        incl_lower_char=True,
        incl_num=True,
        incl_sp_char=True):
    base_strings = ''
    base_strings += 'A' if incl_upper_char else ''
    base_strings += 'b' if incl_lower_char else ''
    base_strings += '1'*len(base_strings) if incl_num else ''
    for i in range(length-len(password)):
        password += base_strings[i % len(base_strings)]
    if incl_sp_char:
        password = password[:-1] + SP_CHARS[0]
    if incl_invalid_char:
        password = password[:-2] + INVALID_CHAR + password[-1]
    return password
