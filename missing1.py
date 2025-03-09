class Solution(object):
    def missingNumber(self, nums):
        for i in range(len(nums)+1):
            flag=0
            for j in nums:
                if(i==j):
                    flag=1
            if(flag!=1):
                return i