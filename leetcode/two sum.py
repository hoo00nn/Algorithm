class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = list(map(lambda x: target - x, nums))
        for i in range(0, len(diff)):
            if diff[i] in nums:
                if i == nums.index(diff[i]):
                    continue
                return [i, nums.index(diff[i])]