# String Rotation
# leecode problem: https://leetcode.com/problems/rotate-string/submissions/



# O(N)
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        return True if A in B+B else False
