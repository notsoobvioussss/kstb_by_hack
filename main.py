s = input()
a = s.split('.')
for i in  range(len(a)):
    if i == 0:
        print(str(i+1)+'.'+a[i]+'.'+' ', end='')
    elif i == len(a)-2:
        print(str(i + 1) + '.' + a[i] + '.' + ' ')
        break
    else:
        print(str(i + 1) + '.'  + a[i] + '.' + ' ', end=' ')