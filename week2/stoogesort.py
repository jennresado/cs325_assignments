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
    Reads input file and writes sorted arrays to stooge.out.
    """

    output = []

    with open('data.txt', 'r') as file:
       for line in file:
            numbers = line.split()
            numbers = [int(i) for i in numbers]  # convert numbers to int
            num_sort = numbers[0]
            integers = numbers[1:]
            stooge_sort(integers, 0, num_sort - 1)
            output.append(integers)
    
    with open('stooge.out', 'w') as writer:
        for line in output:
            numbers = [str(i) for i in line]  # convert numbers to str
            writer.write(" ".join(numbers))
            writer.write("\n")


if __name__ == "__main__":
    main()