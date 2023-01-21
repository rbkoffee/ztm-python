# Builtin functions -v- Methods
Methods are parts of specific datatypes 
i.e. String Methods 
.length
.toupper
.format 
etc...

```python
quote = 'to be or not to be'
print(quote.toupper())
TO BE OR NOT TO BE
print(quote.capitalize())
To be or not to be
print(quote.find('be'))
3 # position in string where this first occurs
print(quote.replace('be','me'))
To me or not to me
# Note that this only exists in this 'run' of the program, it doesn't overwrite the value of the string

```

## Booleans

`bool` is a boolean true/false

```python

name = 'koffee'
is_nerd = False
is_nerd = True 

print(bool(1)) == print(bool('True')) # 1 is true, 0 is false || False
```

