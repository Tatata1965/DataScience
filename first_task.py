import random

def fn_list(l):
    sp = []
    for i in l:
        if i not in sp:
            sp.append(i)
            sp.sort()
    return print(f"Отсортированный по возрастанию список с уникальными значениями: {sp}")


# аргумент функции- заданный список значений типа int
fn_list([55, 66, 88, 33, 2, 5, 3, 3, 3, 3, 8, 9, 44])

#fn_list([random.randint(1, 100) for i in range(30)])