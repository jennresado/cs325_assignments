def merge_sort(arr, num_sort):
    """
    Merge sort an array of based on start time in descending order.

    Args:
        arr: array to be sorted in descending order
        num_sort: length of array
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

    Args:
        arr: array to be sorted in descending order
        arr1: first half of an array to be merged
        arr2: second half of an array to be merged
    """

    i = j = k = 0  # arrays index counters

    # merge in descending order
    while i < len(arr1) and j < len(arr2):
        if arr1[i][1] >= arr2[j][1]:
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


def activity_schedule(S):
    """
    Find the optimal solution for a sorted set S where activity i
    has three numbers: activity number, start time, and finish time.

    Arg: 
        S: sorted set of activities in descending order of start time
    
    Return:
        solution: an optimal solution that maximize the number of
        activities scheduled
    """

    solution = [S[0]]
    n = len(S)
    i = 0

    for m in range(1, n):
        if S[m][2] <= S[i][1]:  # non-overlapping activities
            solution.append(S[m])
            i = m

    return solution


def schedule(d):
    """
    Sort set(s) of activityies in descending order of start time.
    Find optimal solution(s) that maximize(s) the number of 
    activities scheduled.

    Arg:
        d: dict of sets of activities

    Return:
        d: dict of sets of optimal solutions
    """

    for key, value in d.items():
        merge_sort(value, len(value))
        solution = activity_schedule(value)
        d[key] = solution

    return d


def process_txt(filename):
    """
    Reads and procceses txt file.
    
    Args:
        filename: name of txt file to read and process
    
    Return:
        sets: dict of sets of activities
    """

    sets = {}  # sets of activities
    cur = 0  # current set of activities

    with open(filename, 'r') as file:  # process file
        for line in file:
            l = line.strip().split()
            l = [int(i) for i in l]

            if len(l) == 1:
                cur += 1
                sets[cur] = []
            else:
                sets[cur].append(l)

    return sets


def print_solutions(S):
    """
    Prints solution(s) to terminal.

    Args:
        S: dict of optimal solutions
    """

    for key, value in S.items():
        solution = [str(a[0]) for a in reversed(value)]
        print("Set {}".format(key))
        print("Number of activities selected = {}".format(len(solution)))
        print("Activities: {}".format(" ".join(solution)))


def main():
    """
    Reads and processes input file and prints optimal solutions to terminal.
    """

    sets = process_txt("act.txt")
    sets = schedule(sets)
    print_solutions(sets)


if __name__ == "__main__":
    main()