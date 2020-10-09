# 1-2 Check Permutation: Similar problem in LeetCode https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freqs1 = {}
        for a in s1:
            if a in freqs1:
                freqs1[a] += 1
            else:
                freqs1[a] = 1
                
        freqs2 = {}
        for a in s2[:len(s1)]:
            if a in freqs2:
                freqs2[a] += 1
            else:
                freqs2[a] = 1
        
        if freqs1 == freqs2:
                return True
            
        offset = 0
        end = len(s1)
        while(end+offset < len(s2)):
            freqs2[s2[offset]] -= 1
            if freqs2[s2[offset]] == 0:
                freqs2.pop(s2[offset])
            if s2[end+offset] in freqs2:
                freqs2[s2[end+offset]] += 1
            else:
                freqs2[s2[end+offset]] = 1
            if freqs1 == freqs2:
                return True
            offset+=1
            
        return False
