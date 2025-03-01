class Solution(object):
    def removeDuplicates(self, nums):
        unique_nums = sorted(set(nums))  # Remove duplicates and sort
        nums[:len(unique_nums)] = unique_nums  # Modify nums in-place
        return len(unique_nums)