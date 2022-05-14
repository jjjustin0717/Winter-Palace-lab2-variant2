# Winter-Palace - lab 2 - variant 2

## Description

Lab 2: Immutable Algorithms and Data Structure Implementation

Objectives:

- Design algorithms and data structures in immutable styles
- Usage of recursion
- Develop unit and property-based tests

Variant 2:  Dynamic array

1.You can use the built-in list inside node with a fixed size
2.You need to check that your implementation correctly works
with None value
3.You need to implement functions/methods for getting/setting
value by index
4.A user should specify growing factor

1.You have a chunk of memory. The chunk has a capacity
(how many elements it can contain) and length
(how many elements it contains right now).
2.You need to add a new element, but capacity == length.
  You don’t have space for a new element. What will we need to do?
  1.Allocate a new chunk of memory (in Python, usually,
  it looks like [None]*(capacity *growth_factor))
  2.Copy data from the old chunk to the new chunk
  3.Add a new element to the new chunk.

## Group Information

Group Name: Winter Palace

Group members information as follows.

| HDU Number | Name            |
| ---------- | --------------- |
| 212320024  | Chen Chongzhong |
| 212320025  | Zuo Yuexin      |

## Project structure

- `Immutable_DynArray.py` -- implementation of `DynArray` class with all features.
- `Immutable_DynArray_test.py` -- unit and PBT tests for `Immutable_DynArray`.

## Changelog

---

The second lab of CPO
HDU-ID: 212320025
Name: Zuo Yuexin
Date: 2022/05/14

1.Fix some problems.

---

The second lab of CPO
HDU-ID: 212320025
Name: Zuo Yuexin
Date: 2022/05/13

1.Reconstruct the main function of Lab2.


---

The second lab of CPO
HDU-ID: 212320025
Name: Zuo Yuexin
Date: 2022/05/12

1.Complete the main function of Lab2.

2.Raise some problems of Lab2.


## Design notes

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
the pycharm warn me that Access to a protected member _value of a class.
more detail description is showed in Immutable_DynArray.py.

