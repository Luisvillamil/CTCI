#1.5 One Distance Away:
#From book:
    def oneEditAway(word1,word2):
        if abs(len(word1)-len(word2) > 1):
                return False
        s1 = word1 if len(word1) < len(word2) else word2
        s2 = word2 if len(word1) < len(word2) else word1
        index1 = 0
        index2 = 0
        foundDifference = False
        while(index1 < len(s1) and index2 < len(s2)):
            if s1[index1] != s2[index2]:
                if foundDifference:
                    return False
                foundDifference = True
                if len(s1) == len(s2):
                    index1+=1
            else:
                index1 += 1
            index2+=1
        return True
#dp problem in leetcode https://leetcode.com/problems/edit-distance
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        size1,size2 = len(word1), len(word2)
        dp = [[0]*(size2+1) for _ in range(size1+1)]
        dp[0][0] = 0
        for i in range(size1+1): dp[i][0] = i
        for i in range(size2+1): dp[0][i] = i
            
        for i in range(1,size1+1):
            for j in range(1,size2+1):
                dp[i][j] = min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+(word1[i-1]!=word2[j-1]))
        return dp[size1][size2]
