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

```python
basket = [1,2,3,4,5,100]

print('potato' in basket) # Returns false
basket.count(3) # Returns the number of times something appears in a list
basket.sort() # Sorts and _modifies_ list in place alphanumerically
sorted(basket) # Prints a sorted output _without_ modifying the original
basket.reverse() # Reverses the index position and modifies the order of the list 1st becomes Last etc
print(basket[::-1]) # Will reverse in place and not modify the list

# To create a quick list
basket = list(range(100)) # Creates a 100 item list

# .join method allows the addition of a string to an iterable object (list)
basket = ['1','2','3','4','5','100']
sentence =  'potato'.join(basket)
print(sentence)
```

## List Unpacking

`a,b,c *other, d = [1,2,3,4,5,6,7,8,9]`

This allows for you to assign the first `n` items in the list and the last and have the rest as the placeholder `other`

print(a) = 1 # int
print(other) = [4,5,6,7,8] # list
print(d) = 9 # int

Allows you to unpack specific parts of a list at will

# Dictionary -v- List

* Lists are ordered, Dicitonaries aren't. 
* Lists store Values only, Dictionaries are Key:Value stores

## Building dictionaries

- Keys need to be immuatable as they're stored in memory - cannot use lists as keys.
- Keys need to be unique - replicated keys will update the key value.

If you're unsure of the contents of a dictionary - use a `.get` method and don't assume a key value is there and havet he function fail.

Can also use the `in` query - 

```python
user = {
    'basket' : [1,2,3],
    'salutation' : 'Mr.',
    'age' : 20
}

print('basket' in user) = True
# To search keys/values use: 
print('age' in user.keys()) = True
print(20 in user.values()) = True # iterates over keys in dict
print(user.items()) # Prints tuple of all items in dict
user.clear() # scrubs the dict
user2=user.copy() # Creates a new dict using a copy of user
user.pop('age') # Removes this key from the dict
user.popitem() # Removes last k:v from dict in  Py3.7+ 
user.update({'age' : 25}) # Updates key in place, if a new key, adds the key.
```


