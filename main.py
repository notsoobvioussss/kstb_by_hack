s = input()
a = s.split('. ')
a[-1] = a[-1][:-1]
s1 = '\\n'
for i in range(len(a)):
        print(f'{str(i+1)}.{a[i]}.{s1}', end='')