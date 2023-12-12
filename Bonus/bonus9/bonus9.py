password = input('Enter new password: ')
result = {}
if len(password) >= 8:
    result['Length'] = True
else:
    result['Length'] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True

result['digit'] = digit

uc = False
for i in password:
    if i.isupper():
        uc = True

result['upperCase'] = uc

print(result)
if all(result.values()):
    print('Strong Password')
else:
    print('Weak Password')
