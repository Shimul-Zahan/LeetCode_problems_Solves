def reverse_integer(value):
    # 32 bit signed integer higest value : 2,147,483,647
    negative = value < 0
    string  = str(abs(value))[::-1]
    integer = int(string)
    
    if integer > 2147483647:
        return 0
    
    if negative:
        integer = -integer
        return integer
    return integer

print(reverse_integer(1534236469)) # '321'