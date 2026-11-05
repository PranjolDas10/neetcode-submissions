class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a = 0
        b = len(nums)

        while a < b:
            if nums[a] != val:
                a += 1
            else:
                b -= 1
                nums[a] = nums[b]
        return a