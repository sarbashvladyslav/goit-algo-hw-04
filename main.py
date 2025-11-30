import random
from timeit import timeit

# arr_100 = [random.randint(0, 100) for _ in range(100)]
# arr_1000 = [random.randint(0, 1000) for _ in range(1000)]
# arr_10000 = [random.randint(0, 10000) for _ in range(10000)]

def random_list():
    return [random.randint(0, 100) for _ in range(10000)]

def insertion_sort(lst=random_list()):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

def merge_sort(arr=random_list()):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def main():    
    sort_1 = timeit(random_list().sort, number=1)
    sort_10 = timeit(random_list().sort, number=10)
    sort_100 = timeit(random_list().sort, number=100)
    insertion_sort_1 = timeit(insertion_sort, number=1)
    insertion_sort_10 = timeit(insertion_sort, number=10)
    insertion_sort_100 = timeit(insertion_sort, number=100)
    merge_sort_1 = timeit(merge_sort, number=1)
    merge_sort_10 = timeit(merge_sort, number=10)
    merge_sort_100 = timeit(merge_sort, number=100)
    print(f"Час виконання sort за 1 цикл: {sort_1}")
    print(f"Час виконання insertion sort за 1 цикл: {insertion_sort_1}")
    print(f"Час виконання merge sort за 1 цикл: {merge_sort_1}")
    print(f"Час виконання sort за 10 циклів: {sort_10}")
    print(f"Час виконання insertion sort за 10 циклів: {insertion_sort_10}")
    print(f"Час виконання merge sort за 10 циклів: {merge_sort_10}")
    print(f"Час виконання sort за 100 циклів: {sort_100}")
    print(f"Час виконання insertion sort за 100 циклів: {insertion_sort_100}")
    print(f"Час виконання merge sort за 100 циклів: {merge_sort_100}")

main()