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
    Reads input file and writes sorted arrays to merge.out.
    """

    output=[]

    with open('data.txt', 'r') as file:
        for line in file:
            num_sort = int(line.split()[0])
            integers = line.split()[1:]
            merge_sort(integers, num_sort)
            output.append(integers)

    with open('merge.out', 'w') as writer:
        for line in output:
            writer.write(" ".join(line))
            writer.write("\n")

if __name__ == "__main__":
    main()