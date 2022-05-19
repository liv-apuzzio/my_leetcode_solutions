class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            remainder = target - nums[i]
            if remainder in nums:
                if nums[i] == remainder and nums.count(remainder) != 2:
                    continue
                if nums[i] == remainder and nums.count(remainder) == 2:
                    nums.remove(remainder)
                    return [nums.index(nums[i]), nums.index(remainder) + 1]
                    break
                else:
                    return [nums.index(nums[i]), nums.index(remainder)]
