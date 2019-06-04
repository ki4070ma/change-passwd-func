#!/usr/bin/env python

from .check_similarity import similar
from .verify_pswd import verify_pswd


def change_pswd(old_pswd, new_pswd):
    if not verify_pswd(old_pswd):
        # SHOULD NOT be here for old password. Old password must meet password requirements
        print('[NG] Could not change password due to invalid old password')
    elif not verify_pswd(new_pswd):
        print('[NG] Could not change password due to invalid new password')
    elif similar(old_pswd, new_pswd):
        print('[NG] Could not change password due to similar to previous one')
    else:
        print('[OK] Changed password successfully')
        return True
    return False
