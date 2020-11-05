import sys

def BFS(wrestlers, rivalries):
    """
    BFS: Determine whether it is possible to designate some of the
    wrestlers as Babyfaces, and the remainder as Heels, such that
    each rivalry is between a Babyface and a Heel.

    Args:
        wrestlers: list of wrestlers
        rivalries: list of wrestler rivalry pairings

    Return:
        boolean: True, if designations are possible, else False 
        matches: dictionary of wrestlers and pairings
    """
    
    matches = {}  # Graph
    queue = []  # initialize queue

    # Initialize wrestlers
    for wrestler in wrestlers:
        queue.append(wrestler)
        matches[wrestler] = {
            'color': 'white',
            'rivalries': []
        }    

        # Adjacents
        for rivalry in rivalries:
            if rivalry[0] == wrestler:  
                matches[wrestler]['rivalries'].append(rivalry[1])
            elif rivalry[1] == wrestler:
                matches[wrestler]['rivalries'].append(rivalry[0])

    while len(queue) > 0:
        wrestler = queue.pop(0)

        if matches[wrestler]['color'] == 'white':
            matches[wrestler]['color'] = 'blue'

        for rivalry in matches[wrestler]['rivalries']:
            # Create match
            if matches[rivalry]['color'] == 'white' and \
                    matches[wrestler]['color'] == 'blue':
                matches[rivalry]['color'] = 'red'
                queue.append(rivalry)

            # Not possible to designate same category match
            elif matches[rivalry]['color'] == matches[wrestler]['color']:
                return False, {}

    return True, matches


def process_txt(filename):
    """
    Reads and procceses txt file.
    
    Args:
        filename: name of txt file to read and process
    
    Return:
        wrestlers: list of wrestlers
        rivalries: list of rivalries
    """

    wrestlers_count = 0
    rivalries_count = 0
    wrestlers = []
    rivalries = []

    with open(filename, 'r') as file:  # process file
        for line in file:
            l = line.strip().split()

            if len(l) == 1 and wrestlers_count == 0:
                wrestlers_count = int(l[0])
            elif len(wrestlers) != wrestlers_count:
                wrestlers.append(l[0])
            elif len(l) == 1 and rivalries_count == 0:
                rivalries_count = int(l[0])
            elif len(rivalries) != rivalries_count:
                rivalries.append(l)

    return wrestlers, rivalries


def print_solutions(possible, matches):
    """
    If possible is True, prints pairings to terminal.

    Args:
        possible: True, if pairings are possible, else False.
        matches: dictionary of wrestlers
    """

    if possible:
        babyfaces = []
        heels = []
        for key, value in matches.items():
            if value['color'] == 'red':
                heels.append(key)
            else:
                babyfaces.append(key)
        
        print("Yes Possible")
        print("Babyfaces: {}".format(" ".join(babyfaces)))
        print("Heels: {}".format(" ".join(heels)))
    else:
        print("Impossible")


def main():
    """
    Reads and processes input file and prints output to terminal.
    """

    filename = sys.argv[-1]
    wrestlers, rivalries = process_txt(filename)
    possible, matches = BFS(wrestlers, rivalries)
    print_solutions(possible, matches)


if __name__ == '__main__':
    main()