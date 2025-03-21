class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left=0
        for right,x in enumerate(nums):
            if x:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1