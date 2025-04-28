class Solution(object):
    def isPalindrome(self, s):
        s = " ".join(ch for ch in s if ch.isalnum())
        s = s.lower()
        left = 0
        right = len(s)-1
        while left < right:
            if s[left]!= s[right]:
                return False
                break
            left +=1
            right -=1
        else:
            return True 
        