# Given a collection of distinct numbers, return all possible permutations.

# For example,
# [1,2,3] have the following permutations:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: 
            return [[]]
        return [[nums[i]] + j for i in xrange(len(nums)) for j in self.permute(nums[:i]+nums[i+1:])]

print Solution().permute([1,2,3])