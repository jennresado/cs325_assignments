def insert_sort(arr, num_sort):
    """
    Insertion sort an array of integers in descending order.
    """

    for i in range(1, num_sort):
        key = arr[i]  # current val
        cur = i
        pre = i - 1

        # swap if val > previous int
        while int(key) > int(arr[pre]) and pre >= 0:
            arr[cur] = arr[pre]
            arr[pre] = key
            cur -= 1
            pre -= 1


def main():
    """
    Reads input file and writes sorted arrays to insert.out.
    """

    output=[]

    with open('data.txt', 'r') as file:
        for line in file:
            num_sort = int(line.split()[0])
            integers = line.split()[1:]
            insert_sort(integers, num_sort)
            output.append(integers)

    with open('insert.out', 'w') as writer:
        for line in output:
            writer.write(" ".join(line))
            writer.write("\n")

if __name__ == "__main__":
    main()