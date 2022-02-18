# вводим число с клавиатуры
lst = list(input('Ввидите число:'))
lst2 = list('lst')
# Количество элементов в списке
n = len(lst)
print(lst)
print(len(lst))
if n % 2 == 0:
    c = lst[n // 2:]
    b = lst[:n // 2]
    print("четное"+ str(b)+ str(c) )

else:

    b = lst[n // 2:]
    c = lst[:n // 2]

    print("не четное"+ str(b)+ str(c))


