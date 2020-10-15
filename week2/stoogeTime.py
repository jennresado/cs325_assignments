import random
from datetime import datetime


def stooge_sort(arr, l, r):
    """
    Stooge sort an array in ascending order.
    """

    if arr[l] > arr[r]:
        temp = arr[l]  # hold last val to swap
        arr[l] = arr[r]
        arr[r] = temp
    if r - l > 1:
        third = ((r - l + 1)//3)  # find the 1/3rd of length of arr
        stooge_sort(arr, l, r - third)  # sort first 2/3rd of arr
        stooge_sort(arr, l + third, r)  # sort second 2/3rd of arr
        stooge_sort(arr, l, r - third)  # sort first 2/3rd of arr


def main():
    """
    Records runtime of stooge sort function for arrays of size n.
    """

    sizes = [500, 600, 700, 800, 900, 1000, 1100]

    for n in sizes:
        num_sort = n
        integers = [random.randint(0, 10000) for _ in range(n)]
        start_time = datetime.now()
        stooge_sort(integers, 0, num_sort - 1)
        time_elapsed = datetime.now() - start_time
        print("size: " + str(num_sort) + ", time elapsed: " + str(time_elapsed))


if __name__ == "__main__":
    main()