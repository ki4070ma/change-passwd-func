#!/usr/bin/env python

from change_passwd_func.constants import SP_CHARS, MIN_VALID_LENGTH

VALID_PASSWD_BASE = '1aB2'


def create_passwd(incl_str='', length=MIN_VALID_LENGTH, padding_src_str=VALID_PASSWD_BASE, incl_sp_char=True):
    '''Generate password

    Args:
        incl_str(str): Strings added to the HEAD of password. Default is empty str.
        length(int): Length for passwords. Default is `MIN_VALID_LENGTH`
        padding_src_str(str): Strings used for password padding.
            Strings used repeatedly until filling `length`. Default is `VALID_PASSWD_BASE`
        incl_sp_char(bool): Add special char to teh TAIL of password or not.
            Need at least one special char for valid password. Default is True

    Returns:
        str: Genrated password
    '''
    l = len(padding_src_str)
    for i in range(length):
        incl_str += padding_src_str[i % l]
    if incl_sp_char:
        incl_str = incl_str[:-1] + SP_CHARS[0]
    return incl_str
