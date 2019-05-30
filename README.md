# ASSIGNMENT
## HOW TO RUN TEST

```
(setup python environment. eihter py2 or py3)
pip install pytest
cd /path/to/change_passwd_func
py.test
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
```ChangePassword(oldPassword: String, newPassword: String)```

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
