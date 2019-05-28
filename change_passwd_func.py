#!/usr/bin/env python

#import pysnooper

SP_CHAR = ['!', '@', '#', '$', '&', '*']

def change_passwd_func(old_passwd, new_passwd):
    print('old_passwd: {}'.format(old_passwd))
    print('new_passwd: {}'.format(new_passwd))

    if not _verify_passwd(new_passwd):
        print('Could not change password due to invalid password')
        return False
    elif _similar_passwrd(old_passwd, new_passwd):
        print('Could not change password due to similar to previous one')
        return False

    print('Changed password successfully')
    return True

def _verify_passwd(passwd):
    if len(passwd) < 18:
        print('not enough length')
        return False
    if len([False for x in passwd if not (x.isalnum() or x in SP_CHAR)]) > 0:
        print('included invalid char')
        return False
    if not _include_all_patterns(passwd):
        print("didn't include all pattern")
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
        elif x in SP_CHAR:
            special_flg = True
    return upper_flg and lower_flg and num_flg and special_flg


def _similar_passwrd(old_passwd, new_passwd):
    return False

if __name__ == '__main__':
    old_passwd = 'OLD'
    new_passwd = 'NEW'
    change_passwd_func(old_passwd, new_passwd)
