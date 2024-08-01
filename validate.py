import re
from dataclasses import dataclass, fields
from datetime import datetime

class validation:
    def __init__(self):
        pass

    def valid_name(name):
        if name is None:
            print("Name can not be null.")
        if len(name) < 3 or len(name) > 25:
            print("Length of name must be greater then 3 and less then 25")
            return False
        return True

    def pass_valid(password,c_pass):
        if len(password) <= 8:
            print("Your password is not having enough length")
            return False
        if password != c_pass:
            print("Your both password are not equal")
            return False
        if not re.search('[A-Z]', password):
            return False
        if not re.search('[!@#$%^&*]', password):
            return False
        else:
            return True

    def validate_dob(dob):
        try:
            datetime.strptime(dob, '%d/%m/%y')
            return True
        except ValueError:
            return False