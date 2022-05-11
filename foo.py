import copy
from typing import *


class ImmutableDynamicArray:
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

    def __init__(self, lst: List = [], capacity: int = 10, growth_factor: int = 5):
        """
            Initialize the array
        """
        self._start = 0
        self._size = 0
        self._capacity = capacity
        self._array = [None] * self._capacity
        self._growth_factor = growth_factor

        for value in lst:
            self._append(value)

    def __eq__(self, other) -> bool:
        """ equal function """
        if not isinstance(other, ImmutableDynamicArray):
            return False
        if self._capacity != other.capacity():
            return False
        if self._growth_factor != other._growth_factor:
            return False
        if self._size == other.size():
            flag = True
            for i in range(self._size):
                if self._array[i] != other.get_item(i):
                    flag = False
                    break
            return flag
        return False

    def _resize(self, new_capacity: int) -> None:
        """ resize the array to the new capacity """
        array_b = ImmutableDynamicArray(capacity=new_capacity, growth_factor=self._growth_factor)
        for k in range(self._size):
            array_b._append(self._array[k])
        self._array = array_b._array
        self._capacity = new_capacity

    def _append(self, value: Any) -> None:
        """ add element to the end """
        if self._size == self._capacity:
            self._resize(self._growth_factor * self._capacity)
        self._array[self._size] = value
        self._size += 1


def size(array) -> int:
    """ return array size """
    return array._size


def capacity(array) -> int:
    """ return array's capacity """
    return array._capacity


def is_empty(self) -> bool:
    """ if array is empty return true """
    return self._size == 0


def set_growth_factor(self, growth_factor: int):
    """ set growth factor, growth_factor is the multiple when resize array """
    new_array = copy.deepcopy(self)
    new_array._growth_factor = growth_factor
    return new_array


def append(self, value: Any):
    """ add element to the end """
    new_array = copy.deepcopy(self)
    if new_array._size == new_array._capacity:
        new_array._resize(new_array._growth_factor * new_array._capacity)
    new_array._array[new_array._size] = value
    new_array._size += 1
    return new_array


def insert(self, index: int, value: Any):
    """ insert element to the specified index """
    new_array = copy.deepcopy(self)
    # Invalid insert position
    if not 0 <= index < new_array._size:
        raise IndexError('invalid index')
    if new_array._size == new_array._capacity:
        new_array._resize(new_array._growth_factor * new_array._capacity)
    # Move the element from the tail to make a space at index
    for i in range(new_array._size - 1, index - 1, -1):
        new_array._array[i + 1] = new_array._array[i]
    new_array._array[index] = value
    new_array._size += 1
    return new_array


def remove(self, value: Any):
    """ remove the first appear of the value in the array """
    new_array = copy.deepcopy(self)
    for i in range(new_array._size):
        # Find this element
        if new_array._array[i] == value:
            # Forward covering value
            for j in range(i, new_array._size - 1):
                new_array._array[j] = new_array._array[j + 1]
            # The default value changes to None
            new_array._array[new_array._size - 1] = None
            new_array._size -= 1
            return new_array
    raise ValueError('value not found')


def get_item(self, index: int) -> Any:
    """ Gets array elements based on index """
    if not 0 <= index < self._size:
        raise IndexError('invalid index')
    return self._array[index]


def set_item(self, index: int, value: Any):
    """ Sets the indexing element to a specified value """
    new_array = copy.deepcopy(self)
    if not 0 <= index < new_array._size:
        raise IndexError('invalid index')
    new_array._array[index] = value
    return new_array


def to_list(self) -> List:
    """Returns the elements contained in an array as a list"""
    res = []
    if self._size > 0:
        for i in range(self._size):
            res.append(self._array[i])
    return res


def from_list(self, lst: List):
    """ Accepts list append into an array """
    new_array = copy.deepcopy(self)
    for value in lst:
        new_array._append(value)
    return new_array


def find(self, f) -> int:
    """ Find the first element that meets this requirement and return index """
    for i in range(self._size):
        if (f(self._array[i])):
            return i
    return -1


def filter(self, f) -> List:
    """ Call the specified function function for each element and form a new traversable set of elements that return True """
    value = []
    for i in range(self._size):
        if (f(self._array[i])):
            value.append(self._array[i])
    return value


def map(self, f):
    """ Calls the specified function operation for each element in the iterable object """
    new_array = copy.deepcopy(self)
    for i in range(new_array._size):
        new_array._array[i] = f(new_array._array[i])
    return new_array


def reduce(self, f, initial_state):
    """ Calls the specified function function on an iterable object to do some cumulative operations """
    state = initial_state
    for i in range(self._size):
        state = f(state, self._array[i])
    return state


def concatenate(self, dynamic_array):
    """ concatenate two array """
    lst = dynamic_array.to_list()
    new_array = copy.deepcopy(self)
    if dynamic_array.size() > 0:
        for i in range(len(lst)):
            new_array._append(lst[i])
    return new_array


def __iter__(self):
    """ iteration """
    return self


def __next__(self):
    """ iteration, get next element """
    if self._start <= self._size - 1:
        res = self._array[self._start]
        self._start += 1
        return res
    else:
        raise StopIteration
