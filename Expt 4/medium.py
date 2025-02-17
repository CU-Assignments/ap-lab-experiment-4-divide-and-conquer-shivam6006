# Maximum Subarray

class Solution:
    def maxSubArray(self, nums):
        def divide_and_conquer(nums, left, right):
            if left == right:
                return nums[left]
            mid = (left + right) // 2
            left_sum = divide_and_conquer(nums, left, mid)
            right_sum = divide_and_conquer(nums, mid + 1, right)
            cross_sum = self.max_crossing_sum(nums, left, mid, right)
            return max(left_sum, right_sum, cross_sum)

        return divide_and_conquer(nums, 0, len(nums) - 1)
    
    def max_crossing_sum(self, nums, left, mid, right):
        left_sum = float('-inf')
        total = 0
        for i in range(mid, left - 1, -1):
            total += nums[i]
            left_sum = max(left_sum, total)
        
        right_sum = float('-inf')
        total = 0
        for i in range(mid + 1, right + 1):
            total += nums[i]
            right_sum = max(right_sum, total)
        
        return left_sum + right_sum
