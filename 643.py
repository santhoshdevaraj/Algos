# Given an array consisting of n integers, find the contiguous subarray of given length k 
# that has the maximum average value. And you need to output the maximum average value.

# Example 1:
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
# Note:
# 1 <= k <= n <= 30,000.
# # Elements of the given array will be in the range [-10,000, 10,000].

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        curr_sum = max_sum = sum(nums[:k])

        for i in xrange(k, len(nums)):
        	curr_sum = curr_sum + nums[i] - nums[i-k]
        	max_sum = max(curr_sum, max_sum)

        return float(max_sum)/k
