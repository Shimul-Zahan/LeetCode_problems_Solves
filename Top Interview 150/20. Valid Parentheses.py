class Solution:
    def isValid(self, s: str) -> bool:
        
        ''' 
        first we go for first char if it opening brack then we push it to the stack
        if the char is closing bracket then we pop the last element from the stack and match if its a key value pair or not.
        '''
        
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for char in s:
            if char in bracket_map: 
                # we go in this condition only for the closing parantesis  
                # check char is the same of any key of the dict 
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)
                
        return not stack
                
    
sol = Solution()
print(sol.isValid(s = "()"))