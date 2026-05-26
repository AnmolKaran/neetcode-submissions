class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        while left <= right:
            leftitem = s[left].lower()
            rightitem = s[right].lower()
            if rightitem not in "abcdefghijklmnopqrstuvwxyz0123456789":
                right -=1
                continue
            if leftitem not in "abcdefghijklmnopqrstuvwxyz0123456789":
                left +=1
                continue
            if leftitem != rightitem:
                return False
            left +=1
            right -=1

        return True