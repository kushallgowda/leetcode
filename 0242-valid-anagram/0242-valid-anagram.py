class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        countS, countT = {}, {}

        for i in range(len(s)): #building the hashmaps
             #we know both the lens are same
             countS[s[i]] = 1 + countS.get(s[i], 0) #zero is the default value when its not same 
             countT[t[i]] = 1 + countT.get(t[i], 0)
    
        for c in countS: #iterating with keys 
            if countS[c] != countT.get(c,0):
                return False
        return True

        