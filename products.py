# -*- coding: utf-8 -*-
a = ['картофель', 'перец', 'молоко', 'курица', 'кефир', 'дрожжи', 'сухие дрожжи', 'изюм', 'помидоры', 'баранина', 'творог', 'яйца', 'сахар', 'курага', 'зелень', 'бульон', 'кишка', 'гречка', 'сметана', 'рис', 'чеснок', 'минеральная вода', 'соль', 'соленые огурцы', 'лук', 'разрыхлитель', 'морковь', 'томатная паста', 'индейка', 'сливочное масло', 'мука', 'говядина', 'специи', 'ряженка', 'растительное масло', 'вода', 'мед']
slovar = {}
print(len(a))
for i in range(len(a)):
    if len(a[i])<4:
        slovar[a[i][:3]] = i+1
    else:
        slovar[a[i][:4]] = i + 1
s = input().split('*')
for i in s:
    for j in range(len(a)):
        if len (a[j]) <= 4:
            if a[j][:3] in i:
                print(j+1,end='*')
        else:
            if a[j][:4] in i:
                print(j+1,end='*')

