# Tuples
They're immutable - so can't be sorted, reversed or have anything that performs in place modification. 
This comes with a benefit to performance for searching.
They can be printed or cast to a list if needed to be modified

```python
my_tuple = (1,2,3,4,5)
my_tuple[1] = 'z' # error - tuple object doesn't support assignment
print(5 in my_tuple) - True # This is fine.
# Useful for things like coordinates that aren't mutable.
# Assigning values from a tuple similarly to lists

a,b,*other = (1,2,3,4,5)
print(a) = 1 
print(other) = (3,4,5)
```

Tuples only have 2 native methods - count and index.

- count = how many times an item exists in the tuple
- index = position of item in tuple





