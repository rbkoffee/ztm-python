# Lists - (Arrays) a collection of items into a data structure.

```python
random_list = ['a','b',1,2,'c',True]
print(random_list[3])
```

## Slicing

Similarly with strings 
```python
amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]
print(amazon_cart[0::2])

```

Unlike strings - lists are mutable via this command 

`amazon_cart[0] = 'laptop'`

Slicing creates a copy of the list within a new scope unless the variable is overwritten explicitly
To create a copy of this list to overwrite instead of modifying the original you would do

`new_cart = amazon_cart[:]`

### Matrix = list with lists within it (2D Array) - used frequently in ML

```python

matrix = [
    [1,0,1],
    [0,1,0],
    [1,1,0],
]

print matrix([0][1]) # this will go to the first list, 2nd item.

```

## Builtins



Adding `.` dot operations for in place variables

```python
basket = [1,2,3,4,5,100]

basket.append(100) # Adds 100 to the end of the list
basket.insert(3, 100) # Inserts 100 at the 3rd position
basket.extend([100,101,102]) # Iterable addition of items to a list - allows adding a list to list

basket.pop() # Returns the list without the item it's removed from list - default is the last entry in the list, otherwise you can specify index and it returns *that* index
basket.remove(100) # Will remove the value selected - works in place
basket.clear() # Returns items from list
```

Searching in lists - 

```python
basket = [1,2,3,4,5,100]
basket.index(100, 1, 5) - # Returns the index position of the item - starting from the 1st index, ending at the 5th
```

Can use the python keyword `in` to _assert_ that something is in a list and return a BOOL indicating if it's present.
