
# 1.1 Is unique: https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for x in nums:
            if x in freq:
                return True
            else:
                freq[x] = 1

# A good pythonian way to do this:
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
