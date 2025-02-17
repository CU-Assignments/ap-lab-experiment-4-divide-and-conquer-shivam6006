# Longest Increasing Subsequence II

from bisect import bisect_left

class Solution(object):
    def lengthOfLIS(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dp = []
        
        for num in nums:
            pos = bisect_left(dp, num)
            
            if pos == len(dp):
                if pos == 0 or num - dp[-1] <= k:
                    dp.append(num)
            else:
                if pos == 0 or num - dp[pos - 1] <= k:
                    dp[pos] = num
        
        return len(dp)

solution = Solution()
nums1 = [4, 2, 1, 4, 3, 4, 5, 8, 15]
k1 = 3
print(solution.lengthOfLIS(nums1, k1))  

nums2 = [7, 4, 5, 1, 8, 12, 4, 7]
k2 = 5
print(solution.lengthOfLIS(nums2, k2))  

nums3 = [1, 5]
k3 = 1
print(solution.lengthOfLIS(nums3, k3))  