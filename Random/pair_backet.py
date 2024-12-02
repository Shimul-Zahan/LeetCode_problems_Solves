# def pair_brac(string):
#     stack = []
#     i = 0
#     while i < len(string):
#         if string[i] == ']':
#             stack.append('[')
#         else:
#             stack.append(']')
#         i+=1
#     return stack    
    
# print(pair_brac("][]["))
# # pair_brac("][][")

def pair_brac(string):
    stack = []
    open_brac_needed = 0
    close_brac_needed = 0
    
    for char in string:
        if char == '[':
            stack.append('[')  # push opening bracket to the stack
        elif char == ']':
            if stack:  # there's an opening bracket to match
                stack.pop()  # pop matching opening bracket
            else:
                open_brac_needed += 1  # we need an extra opening bracket
    
    close_brac_needed = len(stack)  # remaining unmatched opening brackets
    
    # Output the number of brackets to be added
    return close_brac_needed
    
print(pair_brac("]]][[["))  # Expected output: (1, 1) -> 1 opening, 1 closing bracket needed
