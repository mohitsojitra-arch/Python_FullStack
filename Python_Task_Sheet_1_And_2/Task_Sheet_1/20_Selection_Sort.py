def selection_sort(items):
    n = len(items)
    
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if items[j] < items[min_idx]:
                min_idx = j
                
        if min_idx != i:
            items[i], items[min_idx] = items[min_idx], items[i]
            
    return items

my_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = selection_sort(my_list)
print("Sorted List:", sorted_list)
