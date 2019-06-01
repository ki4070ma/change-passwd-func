#!/usr/bin/env python

import argparse

from change_passwd_func.change_passwd_func import change_passwd_func

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Intent test')
    parser.add_argument('old_passwd', help="Old password to be replaced with new one", type=str)
    parser.add_argument('new_passwd', help='New password', type=str)

    args = parser.parse_args()

    change_passwd_func(args.old_passwd, args.new_passwd)
