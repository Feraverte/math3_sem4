# pip install -r /path/to/requirements.txt
###БИБЛИОТЕКИ###

from matplotlib import pyplot as plt
from math import ceil as upc

###ОБЪЯВЛЕНИЕ ПЕРЕМЕННЫХ###

summa_count = 0
b = []
c = []

###КЛАССЫ###

#Нахождение медианы за O(n log n)
def nlogn_median(l):
    l = sorted(l)
    if len(l) % 2 == 1:
        return upc(len(l) / 2)
    else:
        return ((len(l) / 2) + (len(l) / 2 + 1)) / 2

###ПРОГРАММА###

#Подсчёт количества букв в словах текста.
a = str(input()).replace(',','').replace('.','').replace('—','').replace(';','').split()
print(a)
for i in range(len(a)):
    a[i] = len(a[i])

#Статистический ряд.
print('Статистический ряд: ',' '.join(str(i) for i in list(a)), end = '\n')

#Таблица (стат. ряд).
for i in range(1,max(a)+1):
    print("Слов с ",i," букв.", a.count(i))
    summa_count += a.count(i) # для пункта "Мода", можно использовать длину списка, но мне захотелось ТАК!
    b.append(int(i)) # для пункта "Медиана".
    c.append(int(a.count(i)))

#Вариационный ряд.
a.sort()
print('Вариационный ряд: ',' '.join(str(i) for i in list(a)), end = '\n')

#Размах выборки.
print('Размах выборки: ', max(a) - min(a), end = '\n')

#Мода.
print('Мода: ', summa_count, end = '\n')

#Медиана.
print('Медиана: ', nlogn_median(b), end = '\n')

#График.
plt.plot(b, c)
plt.show()






