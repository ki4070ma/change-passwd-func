#!/usr/bin/env python

from change_passwd_func.change_passwd_func import change_passwd_func

if __name__ == '__main__':
    old_passwd = 'OLD'
    new_passwd = 'NEW'
    change_passwd_func(old_passwd, new_passwd)
