class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i = 0
        j = i + 1
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False