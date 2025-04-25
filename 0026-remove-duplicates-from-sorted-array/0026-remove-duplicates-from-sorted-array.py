class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 1
        for right in range(1,len(nums)):
            if nums[right]!= nums[right-1]:
                #whenver the right pointer element and its previous is not  the   same then it means that we have a unique element.
                nums[left] = nums[right]
                left +=1
        return left         


        