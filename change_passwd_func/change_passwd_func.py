#!/usr/bin/env python

#import pysnooper

from .check_similarity import check_similarity
from .verify_passwd import verify_passwd


def change_passwd_func(old_passwd, new_passwd):
    print('old_passwd: {}'.format(old_passwd))
    print('new_passwd: {}'.format(new_passwd))

    if not verify_passwd(new_passwd):
        print('Could not change password due to invalid password')
        return False
    elif check_similarity(old_passwd, new_passwd):
        print('Could not change password due to similar to previous one')
        return False

    print('Changed password successfully')
    return True


if __name__ == '__main__':
    old_passwd = 'OLD'
    new_passwd = 'NEW'
    change_passwd_func(old_passwd, new_passwd)
