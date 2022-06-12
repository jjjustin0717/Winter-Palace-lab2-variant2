#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Test immutable version
    Next, look at the fragment of immutable library tests.
    Here, we don’t check all that we need.
    For example, we miss:
        • associativity properties;
        • immutability checks;
        • conversation from/to built-in list.
"""
import unittest

from hypothesis import given
import hypothesis.strategies as st
from typing import List, Any, TypeVar, Generic, Iterator

from Immutable_DynArray import DynArray

T = TypeVar('T')


class TestImmutableDynArray(unittest.TestCase, Generic[T]):

    def test_api(self) -> None:
        empty: DynArray[T] = DynArray()
        l1: DynArray[T] = DynArray([None]).concatenate(  # type: ignore
            DynArray([1]).concatenate(empty))  # type: ignore
        l2: DynArray[T] = DynArray([1]).concatenate(  # type: ignore
            DynArray([None]).concatenate(empty))  # type: ignore
        # TODO: conj to add elements to the end
        self.assertEqual(str(empty), "[]")
        self.assertEqual(str(l1), "[None, 1]")
        self.assertEqual(str(l2), "[1, None]")
        self.assertNotEqual(l1, l2)
        self.assertEqual(l1, DynArray([None]).concatenate(
            DynArray([1]).concatenate(empty)))

        self.assertEqual(empty.size(), 0)
        self.assertEqual(l1.size(), 2)
        self.assertEqual(l2.size(), 2)

        self.assertEqual(str(l1.remove(None)), "[1]")
        self.assertEqual(str(l1.remove(1)), "[None]")

        self.assertFalse(empty.is_member(None))
        self.assertTrue(l1.is_member(None))
        self.assertTrue(l1.is_member(1))
        self.assertFalse(l2.is_member(2))

        self.assertEqual(str(l1), str(l2.reverse()))

        self.assertEqual(l1.to_list(), [None, 1])
        self.assertEqual(l1, empty.from_list([None, 1]))

        self.assertEqual(l1.concatenate(l2),
                         empty.from_list([None, 1, 1, None]))
        buf = []  # type: List[Any]
        for e in l1:
            buf.append(e)
        self.assertEqual(buf, [None, 1])
        lst = l1.to_list() + l2.to_list()  # type: List[Any]
        for e in l1.to_list():
            lst.remove(e)
        for e in l2.to_list():
            lst.remove(e)
        self.assertEqual(lst, [])

        # - filter(l, f)
        def f1(n: int) -> bool:
            return n is not None

        self.assertEqual(l1.filter(f1), [1])

        # - map(l, f)
        def f2(n: Any) -> Any:
            if n is None:
                return 'None'
            return n * 2

        self.assertEqual(l1.map(f2).to_list(), ['None', 2])

        # - reduce(l, f)
        self.assertEqual(empty.reduce(lambda st, e: st + e, 0), 0)

        # - empty()
        self.assertTrue(empty.empty(), True)

    def test_size(self) -> None:
        array: DynArray[T] = DynArray()
        array1: DynArray[T] = array.append(0)
        array2: DynArray[T] = array1.append(1)
        array3: DynArray[T] = array2.append(2)
        self.assertEqual(array.size(), 0)
        self.assertEqual(array1.size(), 1)
        self.assertEqual(array2.size(), 2)
        self.assertEqual(array3.size(), 3)

    def test_get_item(self) -> None:
        array: DynArray[T] = DynArray(lst=[0, 1, 2])
        self.assertEqual(array.get_item(0), 0)
        self.assertEqual(array.get_item(1), 1)
        self.assertEqual(array.get_item(2), 2)

    def test_set_item(self) -> None:
        array1: DynArray[T] = DynArray()
        array2: DynArray[T] = array1.append(0)
        array3: DynArray[T] = array2.set_item(0, 7)
        self.assertEqual(array2.get_item(0), 0)
        self.assertEqual(array3.get_item(0), 7)

    def test_remove(self) -> None:
        array1: DynArray[T] = DynArray(lst=[0, 1, 2, 3, 4])
        array2: DynArray[T] = array1.remove(1)
        array3: DynArray[T] = array2.remove(3)
        self.assertEqual(array1.to_list(), [0, 1, 2, 3, 4])
        self.assertEqual(array2.to_list(), [0, 2, 3, 4])
        self.assertEqual(array3.to_list(), [0, 2, 4])

    def test_is_member(self) -> None:
        array: DynArray[T] = DynArray()
        array1: DynArray[T] = array.append(0)
        array2: DynArray[T] = array1.append(1)
        array3: DynArray[T] = array2.append(2)
        self.assertIn(0, array3.to_list())
        self.assertIn(1, array3.to_list())
        self.assertIn(2, array3.to_list())

    def test_reverse(self) -> None:
        array: DynArray[T] = DynArray()
        array1: DynArray[T] = array.append(0)
        array2: DynArray[T] = array1.append(1)
        array3: DynArray[T] = array2.append(2)
        array4: DynArray[T] = array3.reverse()
        self.assertEqual(array4.to_list(), [2, 1, 0])

    def test_to_list(self) -> None:
        array: DynArray[T] = DynArray()
        array1: DynArray[T] = array.append(0)
        array2: DynArray[T] = array1.append(1)
        array3: DynArray[T] = array2.append(2)
        self.assertEqual(array.to_list(), [])
        self.assertEqual(array1.to_list(), [0])
        self.assertEqual(array2.to_list(), [0, 1])
        self.assertEqual(array3.to_list(), [0, 1, 2])

    def test_from_list(self) -> None:
        test_data = [
            [],
            [0],
            [0, 1]
        ]
        for e in test_data:
            array1: DynArray[T] = DynArray()
            array2: DynArray[T] = array1.from_list(lst=e)  # type: ignore
            self.assertEqual(array2.to_list(), e)

        test_data = [
            [],
            ['a'],
            ['a', 'b']
        ]
        for e in test_data:
            array3: DynArray[T] = DynArray()
            array4: DynArray = array3.from_list(lst=e)  # type: ignore
            self.assertEqual(array4.to_list(), e)

    def test_filter(self) -> None:
        def is_even(n: int) -> bool:
            """ Filter function f: callable """
            return n % 2 == 0

        array: DynArray[T] = DynArray(lst=[0, 1, 2, 3, 4])
        self.assertEqual(array.filter(is_even), [0, 2, 4])

    def test_map(self) -> None:
        def increment(n: int) -> int:
            """ Map function f: callable """
            return n + 2

        array: DynArray[T] = DynArray(lst=[0, 1, 2, 3, 4])
        self.assertEqual(array.map(increment).to_list(), [2, 3, 4, 5, 6])

    def test_reduce(self) -> None:
        array1: DynArray[T] = DynArray()
        self.assertEqual(array1.reduce(lambda st, e: st + e, 0), 0)

        array2: DynArray[T] = DynArray()
        array3 = array2.from_list([1, 2, 3])
        self.assertEqual(array3.reduce(lambda st, e: st + e, 0), 6)

    def test_concatenate(self) -> None:
        lst1 = [0, 1, 2]
        lst2 = [3, 4]
        array1: DynArray[T] = DynArray(lst=lst1)
        array2: DynArray[T] = DynArray(lst=lst2)
        array3 = array1.concatenate(array2)
        self.assertEqual(array1.to_list(), [0, 1, 2])
        self.assertEqual(array2.to_list(), [3, 4])
        self.assertEqual(array3.to_list(), [0, 1, 2, 3, 4])

    def test_empty(self) -> None:
        array: DynArray[T] = DynArray()
        self.assertTrue(array.empty(), True)
        array2: DynArray[T] = array.append(1)
        self.assertIsNotNone(array2.to_list(), None)

    def test_next(self) -> None:
        lst = [0, 1, 2, 3, 4]
        array: DynArray[T] = DynArray(lst=lst)

        iteration = iter(array)

        self.assertIsNotNone(next(iteration))

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, a: List[Any]) -> None:
        array: DynArray[T] = DynArray(lst=a)
        b = array.to_list()  # type: List[Any]
        self.assertEqual(a, b)

    @given(st.lists(st.integers()))
    def test_monoid_identity(self, lst: List[Any]) -> None:
        array1: DynArray[T] = DynArray()
        array2: DynArray[T] = DynArray(lst=lst)

        self.assertEqual(array1.concatenate(array2), array2)
        self.assertEqual(array2.concatenate(array1), array2)

    @given(st.lists(st.integers()))
    def test_python_len_and_list_size_equality(self, a: List[Any]) -> None:
        array: DynArray[T] = DynArray(lst=a)
        self.assertEqual(array.size(), len(a))

    def test_iter(self) -> None:
        lst = [1, 2, 3]
        array: DynArray[T] = DynArray(lst=lst)
        tmp = []  # type: List[Any]
        for e in array:
            tmp.append(e)
        self.assertEqual(lst, tmp)
        self.assertEqual(array.to_list(), tmp)
        i = iter(DynArray())  # type: Iterator[Any]
        self.assertRaises(StopIteration, lambda: next(i))


if __name__ == '__main__':
    unittest.main()
