import copy
from typing import *


class DynArray:
    """
    • You can use the built-in list inside node with a fixed size
    • You need to check that your implementation correctly works with None value
    • You need to implement functions/methods for getting/setting value by index
    • A user should specify growing factor

    1. You have a chunk of memory. The chunk has a capacity (how many elements
    it can contain) and length (how many elements it contains right now).
    2. You need to add a new element, but capacity == length. You don’t have space
    for a new element.What will we need to do?
    1. Allocate a new chunk of memory (in Python, usually, it looks like
    [None]*(capacity *growth_factor))
    2. Copy data from the old chunk to the new chunk
    3. Add a new element to the new chunk.
    """

    def __init__(self, lst=None, ini_capacity: int = 5, growth_factor: int = 2):
        """ Initialize the array """
        if lst is None:
            lst = []
        # _xxx means xxx is protected
        # self._start = 0
        self._size = 0
        self._capacity = ini_capacity
        self._array = [None] * self._capacity
        self._growth_factor = growth_factor

        for value in lst:
            self.add(value)

    def __eq__(self, other):
        """ equal function """
        if other is None:
            return False
        if type(other) is not DynArray:
            return False
        for i in range(self.size):
            if self._array[i] != other.get_item(i):
                return False
        return True

    def __str__(self):
        """ for str() implementation """
        dy_array = copy.deepcopy(self)
        for i in range(self._size):
            dy_array.add(str(self._array[i]))
        return dy_array

    def resize(self, new_capacity: int):
        """ resize the array """
        re_array = DynArray(ini_capacity=new_capacity, growth_factor=self._growth_factor)
        for k in range(self._size):
            re_array.add(self._array[k])
        self._array = re_array._array
        self._capacity = new_capacity

    def add(self, value: Any):
        """ add element to the end(No matter data types) """
        if self._size == self._capacity:
            # This is a commonly used scaling rule x = x*2
            self.resize(self._capacity * self._growth_factor)
        self._array[self._size] = value
        self._size += 1

    def get_item(self, index: int) -> Any:
        """ Gets array elements based on index """
        if not 0 < index + 1 <= self._size:
            print('invalid index')
        return self._array[index]

    # @property is used to decoration get_size method
    @property
    def size(self):
        """ return array size """
        return self._size

    @property
    def capacity(self):
        """ return the capacity of array """
        return self._capacity


"""
    It seems we should not access a protected member of class.
    but what i saw in the given pdf you give an example like this:
    class Node(object):
        def __init__(self, value, next)
        self._value = value
        xxx
    def head(n):
        assert type(n) is Node
        return n._value
    i just copy the code in pdf and test it in pycharm.
    the pycharm warn me that Access to a protected member _value of a class
"""


def set_item(array, index: int, value: Any):
    """ Set an element with specific index / key """
    dy_array = copy.deepcopy(array)
    if not 0 < index + 1 <= array.size:
        print('index is out of line')
    dy_array.array[index] = value
    return dy_array


def remove(array, value: Any):
    """ Remove an element (key, index, or value) """
    dy_array = copy.deepcopy(array)
    for i in range(dy_array.size):
        if dy_array.array[i] == value:
            # Forward covering value
            for j in range(i, dy_array.size - 1):
                dy_array.array[j] = dy_array.array[j + 1]
            # The default value changes to None
            dy_array.array[dy_array.size - 1] = None
            dy_array.size -= 1
            return dy_array
    raise ValueError('value not found')


def is_member(array, value):
    """ Is member """
    dy_array = copy.deepcopy(array)
    for i in range(dy_array.size):
        if dy_array.array[i] == value:
            return True
    return False


def reduce(array, f, initial_state):
    """ Reduce process elements and build a value by the function """
    state = initial_state
    for i in range(array.size):
        state = f(state, array.array[i])
    return state


# def reset_growth_factor(array, growth_factor: int):
#     """ reset growth factor(The initial value is 2 and take cumulative multiplication form) """
#     assert type(array) is DynArray
#     dy_array = copy.deepcopy(array)
#     # Here we use deepcopy to return a new object. so it's a immutable way.
#     dy_array.growth_factor = growth_factor
#     return dy_array


# def insert(array, index: int, value: Any):
#     """ add element at given position """
#     dy_array = copy.deepcopy(array)
#     # Check if index is out of line
#     if not 0 < index + 1 <= array.size:
#         print('index is out of line')
#     if dy_array.size + 1 > dy_array.capacity:
#         dy_array.resize(dy_array.growth_factor * dy_array.capacity)
#     # Reshape the array move index+1's element to index+2
#     for i in range(dy_array.size - 1, index - 1, -1):
#         dy_array.array[i + 1] = dy_array.array[i]
#     dy_array.array[index] = value
#     dy_array.size += 1
#     return dy_array


def to_list(array) -> List:
    """ To built-in list """
    arr_list = []
    if array.size > 0:
        for i in range(array.size):
            arr_list.append(array.array[i])
    return arr_list


def from_list(array, lst: List):
    """ From built-in list """
    dy_array = copy.deepcopy(array)
    for value in lst:
        dy_array.append(value)
    return dy_array


# def find(array, f) -> int:
#     """ Find the first element that meets this requirement and return index """
#     for i in range(array.size):
#         if f(array.array[i]):
#             return i
#     return -1


def filter(array, f) -> List:
    """Filter data structure by specific predicate"""
    dy_array = []
    for i in range(array.size):
        if f(array.array[i]):
            dy_array.append(array.array[i])
    return dy_array


def map(array, f):
    """ Map structure by specific function """
    dy_array = copy.deepcopy(array)
    for i in range(dy_array.size):
        dy_array.array[i] = f(dy_array.array[i])
    return dy_array


# def concatenate(array, dynamic_array):
#     """ concatenate two array """
#     lst = dynamic_array.to_list()
#     dy_array = copy.deepcopy(array)
#     if dynamic_array.size() > 0:
#         for i in range(len(lst)):
#             dy_array.append(lst[i])
#     return dy_array


def empty():
    return None


def __iter__(array):
    """ iteration """
    return array


def __next__(array):
    """ iteration, get next element """
    if array.start <= array.size - 1:
        res = array.array[array.start]
        array.start += 1
        return res
    else:
        raise StopIteration
