class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(2):
            for e in nums:
                ans.append(e)
        return ans
            
        


        