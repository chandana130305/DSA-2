class Solution(object):
    def check(self, nums):
        sorted_nums = sorted(nums)
        n = len(nums)
        for i in range(n):  
            if nums[i:] + nums[:i] == sorted_nums:
                return True
        return False