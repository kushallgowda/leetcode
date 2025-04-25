class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0 
        for i in range(len(nums)):
            if nums[i] != val: #if its equal we are not doing anything
                nums[k] = nums[i]
                k +=1
        return k
                