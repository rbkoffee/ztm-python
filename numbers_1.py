# Fundamental Data Types - Int & Float

# Printing output of arithmetic

print(2+4)
print(2*4)
print(2/4)

# Showing floats = pos/neg whole numbers, decimals are floats

print(type(2+4)) #int
print(type(2*4)) 
print(type(2/4)) #float

# Adding float type give a float (even if it's a whole number)

print(9.9+1.1)
print(type(9.9 + 1.1))

# Other Arithmetic Operators 
print(2 ** 3) # x ** y = x to the power of y
print (12 // 5) # Division to lowest int? (Lowest Common Denominator)
print (13 % 2) # Module - remainder

# math functions
print(type(round(3.14))) # Round to nearest int
print(abs(-3.14)) # Absolute ( positive ) float value

Binary & Hexadecimal

# Numbers are stored in memory as binary - this can be output via: 

print(bin(5))

# outputs as 0b101 with '0b<NUM>' showing it's using binary base

# Hex will be output as '0x<NUM>' to show it's using base 16
print(hex(14))

# Converting from hex/bin back to int can be done via int('number','base')
int('0xe',16) # 14
int('0b1101',2) # 13

selfish = '12345678'
        #  01234567
print(selfish[::-1])
