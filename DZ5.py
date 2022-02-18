# вводим число с клавиатуры
lst = list(input('Ввод данных:'))
lst2 = list('lst')
# Количество элементов в списке
n = len(lst)
print(lst)
print("Колличество элиментов в списке",len(lst))
if n % 2 == 0 :

    b = [lst[: n // 2], lst[n // 2:]]
    print("четное")
    print(str(b) )

else:

    c = [lst[: n // 2 + 1 ], lst[n // 2 +1:]]

    print("не четное")
    print(str(c))


