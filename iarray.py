def count_max_elements(arr):
    max_elem = max(arr) # находим максимальный элемент в массиве
    count = 0 # инициализируем счетчик
    for elem in arr: # проходим по всем элементам массива
        if elem == max_elem: # если текущий элемент равен максимальному
            count += 1 # увеличиваем счетчик
    return count # возвращаем количество максимальных элементов

# пример использования функции
arr = [1, 3, 5, 7, 5, 2, 5, 8, 5, 4] # ПОДСТАВИТЬ СВОИ ЗНАЧЕНИЯ
count = count_max_elements(arr)
print("Количество максимальных элементов в массиве:", count)
