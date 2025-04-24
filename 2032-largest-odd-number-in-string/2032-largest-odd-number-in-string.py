class Solution(object):
    def largestOddNumber(self, num):
        j = -1
        for i in range(len(num)-1, -1, -1):
            if int(num[i]) % 2 == 1:
                j = i
                break
        i = 0
        while num[i] == 0 and i < j:
            i +=1
        return num[i:j+1]
        