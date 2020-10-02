import random
from datetime import datetime


def merge_sort(arr, num_sort):
    """
    Merge sort an array of integers in descending order.
    """

    if num_sort > 1:
        mid = len(arr)//2  # divide array in half
        arr1 = arr[:mid]  # first half
        arr2 = arr[mid:]  # second half
        merge_sort(arr1, mid)  
        merge_sort(arr2, num_sort-mid) 
        return [merge(arr, arr1, arr2)] # merge arr1 and arr2 back together


def merge(arr, arr1, arr2):
    """
    Merge two arr1 and arr2 in descending order.
    """

    i = j = k = 0  # arrays index counters

    # merge in descending order
    while i < len(arr1) and j < len(arr2):
        if int(arr1[i]) >= int(arr2[j]):
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        
        k += 1
    
    # merge any remaining integers
    while i < len(arr1):
        arr[k] = arr1[i]
        i += 1
        k += 1
    
    while j < len(arr2):
        arr[k] = arr2[j]
        j += 1
        k += 1


def main():
    """
    Records runtime of merge sort function for arrays of size n.
    """

    sizes = [170000, 180000, 190000, 200000, 210000, 220000, 230000]

    for n in sizes:
        num_sort = n
        integers = [random.randint(0, 10000) for _ in range(n)]
        start_time = datetime.now()
        merge_sort(integers, num_sort)
        time_elapsed = datetime.now() - start_time
        print("size: " + str(num_sort) + ", time elapsed: " + str(time_elapsed))


if __name__ == "__main__":
    main()