# Variables
Binding of values to names that are stored in memory for use later.

* Write using snake_case not camelCase
* Start with lowercase or underscore
* Combination of letters, numbers, underscores ( but not start with a number )
* Case sensitive
* Can't overwrite keywords (int,bool,float etc...)

Other standards - 

- vars starting with underscore _ are private variables
- vars should be descriptive and authoritative for human readability

 Variables can be written in relation to other variables 
i.e. 

```python

user_iq = 210
age = user_iq/4

```
## Constants

Variables declared in capitals - they don't change within the scope of the program.

## Double Underscores - dunders 

These are generally codeblocks/invocations that should be immutable

`__main__`


## Declaration via positional arguments

Positional arguments can allow for the rapid declaration of like variables.

a,b,c = 1,2,3

print(a) = 1
print(b) = 2
print(c) = 3


## Expressions -v- Statements

Expressions produce values, Statements are lines of code that perform actions.

user_age = user_iq/5
           __________ --> This expresses the value of a statement ( expression )
____________________  --> The whole line is a Statement

## Augmented Assignment Operator
Allows for quick manipulation of a previously defined variable
some_value = 6
some_value += 2 is equivalent to some_value = some_value + 2

# Strings

Can be declared with '' , "" , '''  '''
''' can be used for multi-line strings '''

Strings are immutable until the value of the variable they're assigned to is reassigned.

### Concatenation
```python
# Combining two variables of type 'str'
first_name = 'rb'
last_name = 'koffee'
full_name = first_name + ' ' + last_name 

print(full_name)
rb koffee
```

## Type Conversion
Converting one datatype to another
a = str(100)
b = int(a)
c = type(b)

print(c) = int
print(type(a)) = str

## Escape Sequences & delimiters

Adding a \ preceding a field delimiter ( ', " ) will have python interpret it as a string. 
Adding \t and \n add a tab and newline respectively.

## Formatted Strings ( fstrings )

name = 'potato'
age = 55 

```python
#Python3ism
print(f'hi {name}. You are {age} years old') # does type conversion to strings to stop type mismatch issues.
```

Python2 (and 3) can use `.format` to achieve this

```python
print('hi {}. You are {} years old'.format('Johnny', '55')) # uses positional arguments 
print('hi {}. You are {} years old'.format(name,age)) # uses variables
```

## Indexing a string

```python
selfish = '12345678'
        #  01234567
print(selfish[0:7:2])   
1357
```

Slices index from [start:stop:step]
Default values are assumed if not entered; starts at 0, steps by 1, continues until the end
e.g.

```python
[4:] # starts at 5th character and continues by one until the end -> 5678
[:5] # starts at 1st character and continues until the fourth entry prints that and then stops - it doesn't print entry 5 -> 12345
[::-1] # reverses the string
```
