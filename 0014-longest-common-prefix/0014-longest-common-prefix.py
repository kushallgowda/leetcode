class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        ans = []
        first = strs[0]
        last = strs[-1]
        for i in range(0,min(len(first),len(last))):
            if first[i]!=last[i]:
                return "".join(ans)
            ans.append(first[i])
        return "".join(ans)
        