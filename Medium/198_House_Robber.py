'''Link to Problem: https://leetcode.com/problems/house-robber/?envType=study-plan-v2&envId=leetcode-75'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = {}
        ind=0

        def find_all_sums(nums, ind):

            if not nums:
                return 0
            
            if ind in memo:
                return memo[ind]
            
            with_cur = nums[0]  + find_all_sums(nums[2:], ind+2)
            without_cur =  0 + find_all_sums(nums[1:],ind+1)

            if with_cur > without_cur:
                memo[ind] = with_cur
                return with_cur
            else:
                memo[ind] = without_cur
                return without_cur
            
        
        return find_all_sums(nums,ind)

        