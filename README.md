# Winter-Palace - lab 2 - variant 2

## Description

Lab 2: Immutable Algorithms and Data Structure Implementation

Objectives:

- Design algorithms and data structures in immutable styles
- Usage of recursion
- Develop unit and property-based tests

Variant 2:  Dynamic array

- You can use the built-in list inside node with a fixed size
- You need to check that your implementation correctly works
with None value
- You need to implement functions/methods for getting/setting
value by index
- A user should specify growing factor

1. You have a chunk of memory. The chunk has a capacity
(how many elements it can contain) and length
(how many elements it contains right now).
2. You need to add a new element, but capacity == length.
   You don’t have space for a new element. What will we need to do?
    1. Allocate a new chunk of memory (in Python, usually,
    it looks like [None]*(capacity *growth_factor))
    2. Copy data from the old chunk to the new chunk
    3. Add a new element to the new chunk.

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

- 29.03.2022 - 2
  - Add test coverage.
- 29.03.2022 - 1
  - Update README. Add formal sections.
- 29.03.2022 - 0
  - Initial

## Design notes

- ...

