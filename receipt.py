s = input()
a = s.split(', ')
for i in range(len(a)):
    if i == 0:
        print('*'+a[i], end='')
    elif i == len(a)-1:
        print('*' + a[i][:-1])
        break
    else:
        print('*'  + a[i], end='')