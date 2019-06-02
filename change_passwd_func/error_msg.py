#!/usr/bin/env python

from .constants import (
    MAX_CHAR_CONTINUOUS_NUM,
    MAX_SP_CHAR_NUM,
    MAX_VALID_LENGTH,
    MIN_VALID_LENGTH
)


class ErrorMsg(object):

    INVALID_LENGTH = 'The length needs to be from {} to {}.'.format(MIN_VALID_LENGTH, MAX_VALID_LENGTH)

    INVALID_CHAR = 'Included invalid char'

    NOT_ALL_PATTERNS = "All necessary patterns aren't included"

    OVER_CONTINUOUS_SAME_CHARS = 'Included continous more than {} same chars'.format(MAX_CHAR_CONTINUOUS_NUM)

    OVER_SP_CHAR_NUM = 'Included more than {} special characters'.format(MAX_SP_CHAR_NUM)

    MORE_THAN_HALF_OF_LENGTH = '50 % of password should not be a number'
