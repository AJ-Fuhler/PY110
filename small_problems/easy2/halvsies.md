Write a function that takes a list as an argument and returns a list that
contains two elements, both of which are lists. Put the first half of the
original list elements in the first element of the return value and put the
second half in the second element. If the original list contains an odd number
of elements, place the middle element in the first half list.

1. Understanding the Problem

Input: list
Output: list containing two lists as its elements

Requirements:
  
  Explicit:
  - return a list containing two lists:
    - The first list needs to contain the first half of the original list
      elements.
    - The second list needs to contain the second half of the original list
      elements.
    - If the original list contains an odd number of elements, the middle
      elements needs to be placed in the first list

  Implicit:
  -

Questions:

- Can the original list be empty? YES, RETURN TWO EMPTY LISTS
- What if the original list only has one element? ONLY THE FIRST LIST CONTAINS
  AN ELEMENT.

2. Examples and Test Cases:

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])

3. Data Structures

- list containing the first half of original objects elements
- list containing the other half
- list containing these lists to return

4. Algorithm

- given a 'original_list'
- if 'original_list' is empty:
    - return [[], []]
- if the length of 'original_list' = 1:
    - return [[original_list[0]], []]
- if length of 'original_list' % 2 == 0:
    - center_index = length of 'original_list' // 2
- else:
    - center_index = length of 'original_list' // 2 + 1

lst1 = 'original_list' from index 0 to but excluding center_index
lst2 = 'original_list from center_index to end

return [lst1, lst2]