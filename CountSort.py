def count_sort(arr):
    max_el = max(arr)
    temp_arr = [0] * (max_el + 1)


    for i in arr:
        temp_arr[i] += 1
    
    for i in range(1, max_el + 1):
        temp_arr[i] += temp_arr[i -1]

         
    print(temp_arr)
    max_temp_arr = max(temp_arr)
    sorted_arr = [0] * (max_temp_arr)

    for i in arr:
        count = temp_arr[i]
        sorted_arr[count - 1] = i
        temp_arr[i] -= 1

    print(sorted_arr)

arr = [2, 9, 7, 2, 4, 1, 8, 4, 6]

count_sort(arr)

