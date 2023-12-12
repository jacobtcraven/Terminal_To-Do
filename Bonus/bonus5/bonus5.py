waitingList = ['sen', 'ben', 'john']
waitingList.sort()

for index, item in enumerate(waitingList):
    row = f"{index + 1}. {item.capitalize()}"
    print(row)

