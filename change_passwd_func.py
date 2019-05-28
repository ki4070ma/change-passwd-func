#!/usr/bin/env python

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
    elif len([False for x in passwd if not (x.isalnum() or x in ['!', '@', '#', '$', '&', '*'])]) > 0:
        print('included invalid char')
        return False
    return True

def _similar_passwrd(old_passwd, new_passwd):
    return False

if __name__ == '__main__':
    old_passwd = 'OLD'
    new_passwd = 'NEW'
    change_passwd_func(old_passwd, new_passwd)
