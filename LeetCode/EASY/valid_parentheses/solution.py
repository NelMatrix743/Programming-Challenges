class Solution:

    def isValid(self, s: str) -> bool:
        paren: list[str] = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        if s[0] in paren:
            return False
        tracker_stack: list[str] = [] 
        for char in s:
            if char not in paren:
                tracker_stack.append(char)
                continue
            try:          
                if tracker_stack[-1] != paren[char]:
                    return False
                tracker_stack.pop()
            except IndexError:
                return False
        return not len(tracker_stack)
	
# eosc