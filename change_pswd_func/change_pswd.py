#!/usr/bin/env python

from .check_similarity import similar
from .log import LogMsgChangePaswd
from .verify_pswd import verify_pswd


def change_pswd(old_pswd, new_pswd):
    if not verify_pswd(old_pswd):
        # SHOULD NOT be here for old password. Old password must meet password requirements
        print(LogMsgChangePaswd.INVALID_OLD_PSWD)
    elif not verify_pswd(new_pswd):
        '''
        [Change password requirement] New password should be a valid password
        '''
        print(LogMsgChangePaswd.INVALID_NEW_PSWD)
    elif similar(old_pswd, new_pswd):
        print(LogMsgChangePaswd.SIMILAR_TO_OLD_ONE)
    else:
        print(LogMsgChangePaswd.SUCCESS)
        return True
    return False
