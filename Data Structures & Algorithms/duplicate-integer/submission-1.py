class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use a set 
        # if number alr in set then return t, else f

        s = set()
        for n in nums:
            if n in s:
                return True
            else:
                s.add(n)
        return False