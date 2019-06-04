#!/usr/bin/env python


def find_pswd(pswd):
    return pswd in load_system_pswd()


def load_system_pswd(filepath='change_pswd_func/file/pswds_on_system'):
    pswds = []
    with open(filepath, 'r') as fr:
        for line in fr.readlines():
            pswds.append(line.strip())
    return pswds
