import re

def validate_phone_number(number):
    if re.match(r'^01[016789][1-9]\d{6,7}$', number): #r은 raw의 약자
        return True
    return False

print(validate_phone_number('01064006655'))
print(validate_phone_number('010-6400-6655'))
print(validate_phone_number('d1064006655'))
print(validate_phone_number('101010'))