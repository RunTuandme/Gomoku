c = 0
with open('test.txt', 'w') as f:
    for j in range(15):
        for i in range(15):
            x = i*25+7.5
            y = j*25+37.5
            print('\'%3d\':(%5.1f, %5.1f), '%(c, x, y), end='', file=f)
            c += 1
        print ('\n',end='',file=f)