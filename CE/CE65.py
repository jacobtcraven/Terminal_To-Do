file = open('members.txt', 'r')
x = file.readlines()
file.close()

i = input('enter member: ')
x.append(i)

file = open('members.txt', 'w')
file.writelines(x)
file.close()

