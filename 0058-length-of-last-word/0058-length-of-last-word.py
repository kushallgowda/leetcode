class Solution(object):
    def lengthOfLastWord(self, s):
        i = len(s)-1
        length = 0
        #ignore the spaces at the end
        while s[i] == " ":
            i -=1
        #counting the characters
        while s[i] != " " and i >=0:
            length +=1
            i -=1
        return length
        