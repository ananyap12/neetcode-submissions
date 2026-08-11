class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use a map that stores the curr w/ the index
        # if the diff (target - curr) is in the map, return the current
        # index and the index of the diff

        m = {}
        diff = 0
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in m:
                return [m[diff], i]
            m[nums[i]] = i

        return []