#!/usr/bin/env python

from .check_similarity import similar
from .verify_passwd import verify_passwd


def change_passwd_func(old_passwd, new_passwd):
    print('[old_passwd]: {}'.format(old_passwd))  # For debug
    print('[new_passwd]: {}'.format(new_passwd))

    if not verify_passwd(old_passwd):
        # SHOULD NOT be here for old password. Old password must meet password requirements
        print('[NG] Could not change password due to invalid old password')
    elif not verify_passwd(new_passwd):
        print('[NG] Could not change password due to invalid new password')
    elif not similar(old_passwd, new_passwd):
        print('[NG] Could not change password due to similar to previous one')
    else:
        print('[OK] Changed password successfully')
        return True
    return False
