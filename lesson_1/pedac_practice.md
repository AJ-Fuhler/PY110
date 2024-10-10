Leftover Blocks:

1. Understand The Problem:

input: integer of building blocks that can be used to build a valid structure.
output: integer of blocks left over after building the tallest possible valid
structure.

Requirements:
  Explicit:
    - The top layer is a single block
    - A block in an upper layer must be supported by four blocks in a lower
      layer.
    - A block in a lower layer can support more than one block in an upper
      layer.
    - There can't be gaps between blocks.

  Implicit:
   - Layer number correlates with blocks in a layer
   - The number of blocks in a layer is layer number * layer number

Questions:
   - Is a lower layer valid if it has more blocks than it needs? NO
   - Will there always be left-over blocks? NO


2. Examples and Test Cases:

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True

3. Data Structure:

Potentially using a nested list to represent the structure could be helpful?
Each sublist could represent a layer.

[
    ['x'],
    ['x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
      ...
]

4. Algorithm:

High level abstract algorithm:
- Build the structure one layer at a time until you have no blocks left.
- Count how many blocks you have left

Programmatic level algorithm:

- find out if we have enough blocks to make the first layer
- if we can have enough blocks, make the layer
- if we dont, count the amount of leftover blocks and return it.

SET layer_number = 1
While number_blocks > 0:
  if number_blocks - layer_number ** 2 > 0:
    number_blocks -= layer_number ** 2
    layer_number += 1
   else:
     return number_blocks


    