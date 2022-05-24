class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            if target > nums[-1]:
                print(target)
                return nums.index(nums[-1]) + 1
            if target < nums[0]:
                return 0
            if nums[0] < target < nums[-1]:
                for i in range(0, len(nums)):
                    if nums[0] < target < nums[i]:
                        return nums.index(nums[i])