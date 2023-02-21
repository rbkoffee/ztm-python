# Sets

Sets are unordered collections of unique objects. 

```python 
my_set = {1,2,3,4,5}
my_set.add(100)
my_set.add(2) # won't be added because it's not unique
```

This is useful if you want to find unique items in a given list by casting the list to a set. 
`print(set(my_list))`

Cannot find the index of an object within a set (because it's unordered) only that it exists
`print(1 in my_set) #True` 

## Methods

```python
my_set = {1,2,3,4,5}
your_set {3,4,5,6,7,8}

my_set.difference(your_set) # Unique values in my_set
my_set.discard(5) # Modify set to remove object
my_set.difference_update(your_set) # Updates my_set having removed the overlap with your_set
my_set.intersection(your_set) # Where sets overlap can also use & e.g my_set & your_set
my_set.isdisjoint(your_set) # Do sets have nothing in common - are they distinct sets; returns BOOL
my_set.issubset(your_set) # Is my_set wholly contained in your_set
my_set.issuperset(your_set) # Does my_set contain your_set entirely
.union() # Joins sets and creates a new set can also use | e.g. my_set | your_set
```