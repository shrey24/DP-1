'''https://leetcode.com/problems/house-robber/
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint 
stopping you from robbing each of them is that adjacent houses have 
security systems connected and it will automatically contact the police 
if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the 
police.

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
'''

# Time Complexity : O(N)
# Space Complexity : O(N)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
class Solution:
    def rob(self, nums: 'list[int]') -> int:
        # 2 columns: skip , taken
        # n rows for elements of nums
        # dp = [[0, 0]]*len(nums)
        dp = [[0, 0] for _ in range(len(nums))]
        dp[0][1] = nums[0]
        
        for i in range(1, len(nums)):
            # current house not robbed
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]) 
            # current house robbed, 
            dp[i][1] = dp[i-1][0] + nums[i] 
        
        return max(dp[len(nums)-1][0], dp[len(nums)-1][1])
            
        
        
        
        
