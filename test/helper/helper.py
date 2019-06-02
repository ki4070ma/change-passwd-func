#!/usr/bin/env python

from change_passwd_func.constants import MIN_VALID_LENGTH, SP_CHARS


def pswd_generator(pswd_base='', length=MIN_VALID_LENGTH,
                   incl_upper_char=True, incl_lower_char=True, incl_num=True, incl_sp_char=True):
    '''Generate password

    To generate password along to points in below file
    https://docs.google.com/spreadsheets/d/1Gq1EUD5i_Ko0uE9PCUINHnwNm5oDvesw5OMNhHfZT14/edit#gid=0

    However, need to use `pswd_base` to meet 'Duplicate repeat char' and 'Ratio of num in pswd'
    Need to know how password is generated by repeating `base_strings` in below codes.
    TODO: Make easy to understand how password is generated along to args

    Args:
        pswd_base(str): Used string at the HEAD of password
        length(int): Password length in total
        incl_upper_char(bool): Flag to include upper char in password.
            If True, added 1 upper char to `base_strings`
        incl_lower_char(bool): Flag to include lower char in password.
            If True, added 1 lower char to `base_strings`
        incl_num(bool): Flag to include numeric in password.
            If True, added 1 numeric to `base_strings`
        incl_sp_char(bool):Flag to include sp char in password.
            If True, used sp char at the TAIL of password

    Returns:
         str: Genrated password
    '''

    base_strings = ''
    base_strings += 'A' if incl_upper_char else ''
    base_strings += 'b' if incl_lower_char else ''
    base_strings += '1'*len(base_strings) if incl_num else ''
    for i in range(length-len(pswd_base)):
        pswd_base += base_strings[i % len(base_strings)]
    if incl_sp_char:
        pswd_base = pswd_base[:-1] + SP_CHARS[0]
    return pswd_base
