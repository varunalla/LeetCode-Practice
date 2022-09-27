class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        mapping = {")" : "(", "}" : "{" , "]" : "["}
        
        for char in s:
            
            if char in mapping:
                
                if stack:
                    topElement = stack.pop()
                else:
                    topElement = '#'
                
                if mapping[char] != topElement:
                    return False
            else:
                stack.append(char)
                
        return not stack   
