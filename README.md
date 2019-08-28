[![Build Status](https://travis-ci.org/ki4070ma/change-passwd-func.svg?branch=master)](https://travis-ci.org/ki4070ma/change-passwd-func)
[![codecov](https://codecov.io/gh/ki4070ma/change-passwd-func/branch/master/graph/badge.svg)](https://codecov.io/gh/ki4070ma/change-passwd-func)

# Assignment

## Add password requirement
1. At least 18 alphanumeric characters and list of special chars !@#$&*
   * [Add] Maximum length is 1000.
      * Because 1000 is enough as password and would like not to take care of large length like `sys.maxsize` from quality point of view. Too large length password may impact to the system like performance wise.


## How to run test

```
(setup python3 environment)
$ git clone git@github.com:ki4070ma/change-passwd-func.git
$ cd change_passwd_func
$ pip install -r requirements.txt
$ py.test
$ (py.test --capture=no --verbose --cov . --cov-report=html)  # To show details and generate code coverage report
```

## Test design and Test cases
Used decision table to check coverage

* For verify_pswd, find_pswd, check_similarity, change_pswd
    * https://docs.google.com/spreadsheets/d/1Gq1EUD5i_Ko0uE9PCUINHnwNm5oDvesw5OMNhHfZT14/edit?usp=sharing

## Others
* You can try ```main.py``` as below

```bash
$python3 main.py "\!12Ab11Ab11Ab11Ab11Ab" "\!12Ab11Ab11abcdefghij"

[pswd]: !12Ab11Ab11abcdefghij
[OK] Valid password

[string1]: !12Ab11Ab11Ab11Ab11Ab
[string2]: !12Ab11Ab11abcdefghij
[OK] Changed password successfully
```

# Objective
We want you to create a change password function based on below specification.
This change password function will just return True or False back to function caller to inform the caller
whether the password can be changed successfully or not. For the old password requirement you can do
it as a simple mock function. Apart from the change password function you may need to write the
automate test for the created function as well.

Instructions：
* You can use your choice of programming language
* Hosting on your personal GitHub page, starting from the initial commit is expected
* A simple README, with necessary setup instruction and note on any peculiar cases handled will
be appreciated

# Change password function
## Requirements
* ```ChangePassword(oldPassword: String, newPassword: String)```
   * [py] ```change_pswd(old_pswd: str, new_pswd: str) -> bool```

## Tasks
Please complete the point below
1. Code for change password function
2. Implement automate test for the created function, test cases with test data provide in each case
3. The verify password with system and similar check function should be a mock which return True/False

## Password requirement
1. At least 18 alphanumeric characters and list of special chars !@#$&*
2. At least 1 Upper case, 1 lower case ,least 1 numeric, 1 special character
3. No duplicate repeat characters more than 4
4. No more than 4 special characters
5. 50 % of password should not be a number

## Change password requirement
1. Old password should match with system
2. New password should be a valid password
3. password is not similar to old password < 80% match.
