head = 0
tail = 0
total = 0
while True:
    flip = input('Throw the coin and enter head or tail here: ? ')

    match flip:
        case 'head':
            head += 1
            total += 1
            percent = head / total * 100
            print('Heads: ' + str(percent) + '%')
        case 'tail':
            tail += 1
            total += 1
            percent = head / total * 100
            print('Heads: ' + str(percent) + '%')
        case 'exit':
            break
