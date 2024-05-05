class Item(object):
    """
    Item
    """
    
    def __init__(self, n, v, w):
        """
        Constructor

        Requires:
        n string, represents name;
        v float, represents value;
        w float, represents weight.
        Ensures:
        object of type Item created with given parameters.
        """
        self._name = n
        self._value = float(v)
        self._weight = float(w)
        
    def getName(self):
        """
        Name of item

        Ensures:
        Name of item
        """
        return self._name
    
    def getValue(self):
        """
        Value of item

        Ensures:
        Value of item
        """
        return self._value
    
    def getWeight(self):
        """
        Weight of item

        Ensures:
        Weight of item
        """
        return self._weight
    
    def __str__(self):
        """
        String representation of Item

        Ensures:
        String representation of Item in format
        < name, value, weight>
        """
        result = '<' + self._name + ', ' + str(self._value)\
                 + ', ' + str(self._weight) + '>'
        return result


def value(item):
    """
    Value of a given item

    Requires:
    item Item
    Ensures:
    Value of given item
    """
    return item.getValue()


def weightInverse(item):
    """
    Inverse of weight of a given item

    Requires:
    item Item
    Ensures:
    Inverse of weight of given item
    """
    return 1.0/item.getWeight()


def density(item):
    """
    Density of a given item

    Requires:
    item Item
    Ensures:
    Density of given item
    """
    return item.getValue()/item.getWeight()


def buildItems():
    """
    List of items

    Ensures:
    List with items
    <clock, 175, 10>
    <painitng, 90, 9>
    <radio, 20, 4>
    <vase, 50, 2>
    <book, 10, 1>
    <computer, 200, 20>
    """
    names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
    values = [175, 90, 20, 50, 10, 200]
    weights = [10, 9, 4, 2, 1, 20]
    Items = []
    for i in range(len(values)):
        Items.append(Item(names[i], values[i], weights[i]))
    return Items





## greedy

#def greedy(items, maxWeight, keyFunction, p): # ex 8.3
def greedy(items, maxWeight, keyFunction):
    """
    Knapsack filling for given items, constraint and
    auxiliary function - solving with greedy algorithm

    Requires:
    items list of Items;
    maxWeight float, represents contraint of greedy
    algorithm, i.e. capacity of knapsack in terms of maximum weight;
    keyFunction function, representing auxiliary function
    for selection.
    Ensures:
    Knapsack filled with maximum possible agregated value
    of items up to the maxWeight capacity of knapsack
    along keyFunction auxiliary function, according
    to greedy algorithm (local maximum).
    """
    itemsCopy = sorted(items, key=keyFunction, reverse = True)
    result = []
    totalValue = 0.0
    totalWeight = 0.0
    for i in range(len(itemsCopy)):
#        if (itemsCopy[i].getWeight() <= p and totalWeight + itemsCopy[i].getWeight()) # ex 8.3 <= maxWeight:
        if (totalWeight + itemsCopy[i].getWeight()) <= maxWeight:
            result.append(itemsCopy[i])
            totalWeight += itemsCopy[i].getWeight()
            totalValue += itemsCopy[i].getValue()
    return (result, totalValue)





def testGreedy(items, constraint, keyFunction):
    """
    Testing greedy algorithm to solve knapsack filling

    Requires:
    items list of Item;
    constraint float, represent capacity of knapsack
    in terms of maximum weight;
    keyFunction function, auxiliary function for selection
    Ensures:
    Print to stdout knapsack filled along greedy fucntion.
    """
    taken, val = greedy(items, constraint, keyFunction)
    print('Total value of items taken = ', val)
    for item in taken:
        print(' ', item)


def testGreedys(maxWeight = 20):
    """
    Testing greedy algorithm to solve knapsack filling
    with 20 maximum weight, and with 3 auxilary functions
    for selection.

    Requires:
    maxWeight float, representing capacity of knapsack
    in terms of maximum capacity
    Ensures:
    Print to stdout knapsack filled along greedy fucntion
    with each auxiliary function value, weightInverse and
    density
    """
    items = buildItems()
    print('Use greedy by value to fill knapsack of size', maxWeight)
    testGreedy(items, maxWeight, value)
    print('\nUse greedy by weight to fill knapsack of size', maxWeight)
    testGreedy(items, maxWeight, weightInverse)
    print('\nUse greedy by density to fill knapsack of size', maxWeight)
    testGreedy(items, maxWeight, density)

#testGreedys()


## brute force


def getBinaryRep(n, numDigits):
    """
    Binary representation of a given decimal integer

    Requires:
    n int >= 0
    numDigits int, representing the number of digits
    in binary representation
    Ensures:
    String of length numDigits that is the binary
    representation of n
    """
    result = ''
    while n > 0:
        result = str(n%2) + result
        n = n//2
    if len(result) > numDigits:
        raise ValueError('not enough digits')
    for i in range(numDigits - len(result)):
        result = '0' + result
    return result


def genPowerset(L):
    """
    Power set of a given set

    Requires:
    L list
    Ensures:
    List Power(L)
    """
    powerset = []
    for i in range(0, 2**len(L)):
        binStr = getBinaryRep(i, len(L))
        subset = []
        for j in  range(len(L)):
            if binStr[j] == '1':
                subset.append(L[j])
        powerset.append(subset)
    return powerset






def chooseBest(pset, maxWeight, getVal, getWeight):
    """
    Knapsack filling for given items and constraint - solving
    with brute force algorithm

    Requires:
    pset list, with power list of list of Items;
    maxWeight float, represents contraint of chooseBest
    algorithm, i.e. capacity of knapsack in terms of maximum weight;
    getVal function getVal;
    getWeight function getWeight.
    Return:
    Knapsack filled with maximum possible agregated value
    of items up to the maxWeight capacity of knapsack
    along keyFunction auxiliary function, according
    to brute force algorithm (global maximum).
    """
    bestVal = 0.0
    bestSet = None
    for items in pset:
        itemsVal = 0.0
        itemsWeight = 0.0
        for item in items:
            itemsVal += getVal(item)
            itemsWeight += getWeight(item)
        if itemsWeight <= maxWeight and itemsVal > bestVal:
            bestVal = itemsVal
            bestSet = items
    return (bestSet, bestVal)











def testBest(maxWeight = 20):
    """
    Testing brute force algorithm to solve knapsack filling
    with 20 maximum weight.

    Requires:
    maxWeight float, representing capacity of knapsack
    in terms of maximum capacity
    Ensures:
    Print to stdout knapsack filled along chooseBest function.
    """
    items = buildItems()
    pset = genPowerset(items)
    taken, val = chooseBest(pset, maxWeight, Item.getValue, Item.getWeight)
    print('\nUse optimal solution (brute force) to fill knapsack of size', maxWeight)
    print('Total value of items taken =', val)
    for item in taken:
        print(item)


testBest()



















