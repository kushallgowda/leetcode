class Solution(object):
    def majorityElement(self, nums):
        count = {}
        res, maxcount = 0, 0 #maxcunt is current macode
        for n in nums:
            count[n] = 1 + count.get(n,0)
            if count[n] > maxcount:
                res = n
            else:
                res = res
            maxcount = max(count[n],maxcount)
        return res