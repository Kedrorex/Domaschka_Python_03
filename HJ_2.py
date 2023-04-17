# Задача 18: Требуется найти в списке A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в списке. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

size = int(input("Введите количество элементов массива N: "))
some_list = list(range(1,size+1))
print(some_list)

numberX = int(input("Введите число Х: "))
maxX = numberX - some_list[0]
number = 1


for i in range(1, len(some_list)):
    
    if maxX  >  numberX - some_list[i]:
        if maxX > 0:
            maxX = numberX - some_list[i]
            number = some_list[i]
            
print("Cамый близкий по величине элемент к заданному числу X: ", number)