this_file = __file__


def make_adder_inc(a):
    """
    >>> adder1 = make_adder_inc(5)
    >>> adder2 = make_adder_inc(6)
    >>> adder1(2)
    7
    >>> adder1(2) # 5 + 2 + 1
    8
    >>> adder1(10) # 5 + 10 + 2
    17
    >>> [adder1(x) for x in [1, 2, 3]]
    [9, 11, 13]
    >>> adder2(5)
    11
    """
    helper = -1
    def add_helper(b):
        nonlocal helper
        helper += 1
        return a + b + helper

    return add_helper

def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    >>> from construct_check import check
    >>> # Do not use lists in your implementation
    >>> check(this_file, 'make_fib', ['List'])
    True
    """
    "*** YOUR CODE HERE ***"
    help_1 = 0
    help_2 = 1
    index = 0
    def fib_helper():
        nonlocal help_1
        nonlocal help_2
        nonlocal index
        if index==0:
            index +=1
            return 0
        elif index ==1:
            index+=1
            return 1
        next = help_1+help_2
        help_1 = help_2
        help_2 = next
        return next
    
    return fib_helper



def insert_items(lst, entry, elem):
    """
    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> new_lst = insert_items(test_lst, 5, 7)
    >>> new_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> large_lst = [1, 4, 8]
    >>> large_lst2 = insert_items(large_lst, 4, 4)
    >>> large_lst2
    [1, 4, 4, 8]
    >>> large_lst3 = insert_items(large_lst2, 4, 6)
    >>> large_lst3
    [1, 4, 6, 4, 6, 8]
    >>> large_lst3 is large_lst
    True
    """
    "*** YOUR CODE HERE ***"
    if entry not in lst:
        return lst
    else :
        lenth = len(lst)
        Index=0
        while Index<lenth:
            if lst[Index]==entry:
                lst.insert(Index+1,elem)
                Index +=2
                lenth+=1
            else:
                Index+=1
        return lst
    

