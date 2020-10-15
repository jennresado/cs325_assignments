class Node():
    def __init__(self, key, value, parent, direction):
        """
        Initializes a new Node with specified key, value, parent, and direction.

        Args:
            key: item number
            value: current maximum optimal price
            parent: parent node from which part of current Node's value is derived from
            direction: direction of parent node in knapsack matric
        """
        self.key = key
        self.value = value
        self.parent = parent
        self.direction = direction


class Family():
    def __init__(self):
        """
        Initializes a new Family object.
        """
        self.size = 0
        self.items_count = 0
        self.items = []
        self.weights = []
        self.cart = {}
        self.total_price = 0


def grab_items(s, p, n, w, basket):
    """"
    Helper function: Return the items and total price that would 
    maximize price for total capacity weight and items for a person.

    Args:
        s: set of items (price, weight)
        p: knapsack algorithm matric
        n, w: current indices
        basket: a dictionary with items and total cost
    
    Return:
        basket: a dicionary with items and total cost
    """

    if n == 0 or w == 0:
        return

    grab_items(s, p, p[n][w].parent[0], p[n][w].parent[1], basket)
    if p[n][w].direction == "diagonal":
        basket['items'].append(str(p[n][w].key))
        basket['total_price'] += s[p[n][w].key - 1][0]

    return basket


def maximize_price(n, s, max_weight):
    """
    Helper function: Calculate the items that would maximize price 
    for total capacity weight and items for a person.

    Args:
        s: set of items (price, weight)
        n: number of items
        max_weight: maximum weight for a person
    
    Return:
        basket: a dicionary with items and total cost
    """

    # matrix for 0-1 knapsack algorithm
    p = [[None for w in range(max_weight + 1)] for n in range (n + 1)]  

    for w in range(max_weight + 1):
        p[0][w] = Node(0, 0, None, None)  # 0 items
    
    for n in range(n + 1):
        p[n][0] = Node(n, 0, None, None)  # 0 weights

    for n in range(1, n + 1):
        for w in range(1, max_weight + 1):
            item_weight = s[n - 1][1]
            item_price = s[n - 1][0]

            if item_weight <= w:  # item n can be a part of the solution
                if item_price + p[n - 1][w - item_weight].value > p[n - 1][w].value:
                    p[n][w] = Node(
                        n, 
                        item_price + p[n - 1][w - item_weight].value,
                        [n - 1, w - item_weight],
                        "diagonal"
                        ) 
                else:
                    p[n][w] = Node(
                        n, 
                        p[n - 1][w].value,
                        [n - 1, w],
                        "lateral"
                        )
            else: # item n is too expensive
                p[n][w] = Node(
                    n, 
                    p[n - 1][w].value,
                    [n - 1, w],
                    "lateral"
                    ) 

    # return actual items
    basket = grab_items(s, p, n, max_weight, {'items': [], 'total_price': 0, 'total_weight': 0})

    return basket


def shop(family):
    """
    Calculate and return items that would maximize price for total capacity weight
    and items per person in a family.

    Args:
        family: a Family object
    
    Return:
        family: a Family object
    """

    for i in range(family.size):
        basket = maximize_price(family.items_count, family.items, family.weights[i])
        family.cart[i + 1] = basket['items']
        family.total_price += basket['total_price']

    return family


def process_txt(filename):
    """
    Reads and procceses txt file.
    
    Args:
        filename: name of txt file to read and process
    
    Return:
        cases: an array of Family objects
    """

    cases = []

    with open(filename, 'r') as file:
        family = Family()

        for count, line in enumerate(file):
            l = line.strip().split()
            l = [int(i) for i in l]

            if count == 0:  # number of test cases
                pass
            elif family.items_count == 0:  # number of items
                family.items_count = l[0]
            elif len(l) == 2:  # items
                family.items.append((l[0], l[1]))
            elif len(family.items) == family.items_count and family.size == 0:  # family size
                family.size = l[0]
            elif family.size and len(family.weights) <= family.size:  # weight per family member
                family.weights.append(l[0])

                if family.size == len(family.weights):
                    family = shop(family)
                    cases.append(family)

                    family = Family()  # next family
    
    return cases


def write_txt(output, filename):
    """
    Writes output to shopping.txt.

    Args:
        output: proccessed Family objects
        filename: file name to save output
    """

    with open(filename, 'w') as writer:
        count = 1
        for case in output:
            writer.write("Test Case {}\n".format(count))
            writer.write("Total Price {}\n".format(case.total_price))
            writer.write("Member Items\n")
            
            for key, value in case.cart.items():
                writer.write("{}: {}\n".format(key, " ".join(value)))
            
            writer.write("\n")
            count += 1


def main():
    """
    Reads and processes input file and writes maximized price for total capacity w
    and items per person in a family.
    """

    output = process_txt("shopping.txt")
    write_txt(output, "results.txt")


if __name__ == "__main__":
    main()