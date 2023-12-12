li = ['doc.txt', 'members.txt']

for filename in li:
    file = open(filename, 'r')
    x = file.read()
    print(x)
    file.close()