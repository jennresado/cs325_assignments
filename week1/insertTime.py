import random
from datetime import datetime


def insert_sort(arr, num_sort):
    """
    Insertion sort an array of integers in descending order.
    """

    for i in range(1, num_sort):
        key = arr[i]  # current val
        cur = i
        pre = i - 1

        # swap if val > previous int
        while key > arr[pre] and pre >= 0:
            arr[cur] = arr[pre]
            arr[pre] = key
            cur -= 1
            pre -= 1


def main():
    """
    Records runtime of insert sort function for arrays of size n.
    """

    sizes = [8000, 12000, 16000, 20000, 24000, 28000, 32000]

    for n in sizes:
        num_sort = n
        integers = [random.randint(0, 10000) for _ in range(n)]
        start_time = datetime.now()
        insert_sort(integers, num_sort)
        time_elapsed = datetime.now() - start_time
        print("size: " + str(num_sort) + ", time elapsed: " + str(time_elapsed))


if __name__ == "__main__":
    main()