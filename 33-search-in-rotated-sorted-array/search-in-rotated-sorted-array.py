class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0 ,len(nums) -1
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            if nums[l] <= nums[m]:
                #left
                if target < nums[l] or target > nums[m]:
                    #go to right
                    l = m + 1
                else:
                    #stay left
                    r = m - 1
            else:
                if target > nums[r] or target < nums[m]:
                    #go to left
                    r = m -1
                else:
                    #right
                    l = m + 1
        return -1



            