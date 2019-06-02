#!/usr/bin/env python

from change_passwd_func.change_passwd_func import change_passwd_func

class TestChangePasswd(object):

    def test_change_passwd_OK(self):
        old_passwd = '1aBcDeFgHiJkLmNoPqRsTuV!'
        new_passwd = '1aBcDeFgHiJkLmNoPqRsTuV!1234'
        assert change_passwd_func(old_passwd, new_passwd)

    def test_change_passwd_NG(self):
        old_passwd = '1aBcDeFgHiJkLmNoPqRsTuV!'
        new_passwd = '1aBcDeFgHiJkLmNoPqRsTuV!123456'
        assert not change_passwd_func(old_passwd, new_passwd)
