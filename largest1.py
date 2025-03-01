class Solution:
    def largest(self, arr):
        lar=arr[0]
        for num in arr:
            if num>lar:
                lar=num
        return lar
        