class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        s=n*(n+1)/2
        a=0
        for i in range(n):
            a+=nums[i]
        return s-a
        
