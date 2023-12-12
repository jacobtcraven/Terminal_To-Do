try:
    tot = float(input('input'))
    val = float(input('value'))
    print(val/tot)
except ZeroDivisionError:
    print('Your total value cannot be zero')