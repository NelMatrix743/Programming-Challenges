class Solution(object):

    # Converting int to str
    def isPalindrome(self, x: int) -> bool:
        num_str: str = str(x)
        a = 0
        b = len(num_str) - 1
        while a < b:
            if num_str[a] != num_str[b]:
                return False
            a += 1; b -= 1
        return True

# eosc