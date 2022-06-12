import copy
from typing import Any, Callable, List, Union, TypeVar, Generic, Optional

T = TypeVar('T')
T1 = TypeVar('T1', bound=Union[None, str, int, float])


class DynArray(Generic[T]):
    """
        • You can use the built-in list inside node with a fixed size
        • You need to check that your implementation correctly works
          with None value
        • You need to implement functions/methods for getting/setting
          value by index
        • A user should specify growing factor

        1. You have a chunk of memory. The chunk has a capacity
        (how many elements it can contain) and length
        (how many elements it contains right now).
        2. You need to add a new element, but capacity == length.
        You don’t have space for a new element.What will we need to do?
            1. Allocate a new chunk of memory (in Python, usually,
            it looks like [None]*(capacity *growth_factor))
            2. Copy data from the old chunk to the new chunk
            3. Add a new element to the new chunk.
    """

    def __init__(self, lst: Optional[List[T1]] = None,
                 init_capacity: int = 5, growth_factor: int = 2):
        """ Initialize the array """
        if lst is None:
            lst = []
        # _xxx means property(xxx) is protected
        self._start = 0
        self._size = 0
        self._capacity = init_capacity
        self._array = [None] * self._capacity
        self._growth_factor = growth_factor

        for value in lst:
            self._append(value)

    def __eq__(self, other: object) -> bool:
        """ Equal function """
        if other is None:
            return False
        if type(other) is not DynArray:
            return False
        for i in range(self._size):
            if self._array[i] != other.get_item(i):
                return False
        return True

    def __str__(self) -> str:
        """ For str() implementation """
        dy_array = copy.deepcopy(self)
        for i in range(self._size):
            dy_array.append(self._array[i])
        return str(dy_array.to_list())

    def size(self) -> int:
        """ Return size """
        return self._size

    def capacity(self) -> int:
        """ Return capacity """
        return self._capacity

    def resize(self, new_capacity: int) -> None:
        """ Resize the Dynamic array """
        re_array: 'DynArray[T]' = DynArray(init_capacity=new_capacity,
                                           growth_factor=self._growth_factor)
        for k in range(self._size):
            re_array._append(self._array[k])
        self._array = re_array._array
        self._capacity = new_capacity

    def _append(self, value: Any) -> None:
        """
            When initializing the Dynamic array, lst is not None.
            append the element to the end (No matter data types)
        """
        if self._size == self._capacity:
            # This is a commonly used scaling rule x = x * 2
            self.resize(self._capacity * self._growth_factor)
        self._array[self._size] = value
        self._size += 1

    def append(self, value: Any) -> 'DynArray[T]':
        """ Append the element to the end (No matter data types) """
        array_copy = copy.deepcopy(self)
        if array_copy._size == array_copy._capacity:
            array_copy.resize(array_copy._capacity * array_copy._growth_factor)
        array_copy._array[array_copy._size] = value
        array_copy._size += 1
        return array_copy

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

    def get_item(self, index: int) -> Optional[T1]:
        """ Get array elements based on index """
        if not 0 < index + 1 <= self._size:
            print('invalid index')
        return self._array[index]

    def set_item(self, index: int, value: Any) -> 'DynArray[T]':
        """ Set an element with specific index / key """
        dy_array = copy.deepcopy(self)
        if not 0 < index + 1 <= dy_array._size:
            print('index is out of line')
        dy_array._array[index] = value
        return dy_array

    def remove(self, value: T1) -> 'DynArray[T]':
        """ Remove an element (key, index, or value) """
        dy_array = copy.deepcopy(self)
        for i in range(dy_array._size):
            if dy_array._array[i] == value:
                # Forward covering value
                for j in range(i, dy_array._size - 1):
                    dy_array._array[j] = dy_array._array[j + 1]
                # The default value changes to None
                dy_array._array[dy_array.size() - 1] = None
                dy_array._size -= 1
                return dy_array
        raise ValueError('value not found')

    def is_member(self, value: T1) -> bool:
        """ Is member of Dynamic array """
        dy_array = copy.deepcopy(self)
        for i in range(dy_array.size()):
            if dy_array._array[i] == value:
                return True
        return False

    def reverse(self) -> 'DynArray[T]':
        """ Reverse the Dynamic array for ordered """
        array_copy = copy.deepcopy(self)
        lst = array_copy._array[::-1]
        lst2 = lst[-array_copy._size:]
        dy_array = DynArray(lst2)  # type: DynArray[T]
        return dy_array

    def to_list(self) -> List[T1]:
        """ To built-in list """
        arr_list = []  # type: List[Any]
        if self.size() > 0:
            for i in range(self.size()):
                arr_list.append(self._array[i])
        return arr_list

    def from_list(self, lst: List[T1]) -> 'DynArray[T]':
        """ From built-in list """
        dy_array = copy.deepcopy(self)
        for value in lst:
            dy_array._append(value)
        return dy_array

    def filter(self, f: Callable[..., Any]) -> List[T1]:
        """ Filter data structure by specific predicate """
        lst = []  # type: List[Any]
        for i in range(self.size()):
            if f(self._array[i]):
                lst.append(self._array[i])
        return lst

    def map(self, f: Callable[..., Any]) -> 'DynArray[T]':
        """ Map structure by specific function """
        dy_array = copy.deepcopy(self)
        for i in range(dy_array.size()):
            dy_array._array[i] = f(dy_array._array[i])
        return dy_array

    def reduce(self, f: Callable[..., Any], initial_state: T) -> T:
        """ Reduce process elements and build a value by the function """
        state = initial_state
        for i in range(self._size):
            state = f(state, self._array[i])
        return state

    def concatenate(self, array: 'DynArray[T]') -> 'DynArray[T]':
        """ Concatenate the two Dynamic arrays """
        lst = array.to_list()  # type: List[Any]
        array_copy = copy.deepcopy(self)
        if array.size() > 0:
            for i in range(len(lst)):
                array_copy._append(lst[i])
        return array_copy

    def empty(self) -> bool:
        """ Empty Dynamic array return True """
        return self._size == 0

    def __iter__(self) -> 'DynArray[T]':
        """ Iteration """
        return self

    def __next__(self) -> Optional[T1]:
        """ Iterator, get next element """
        if self._start <= self._size - 1:
            res = self._array[self._start]
            self._start += 1
            return res
        else:
            raise StopIteration
