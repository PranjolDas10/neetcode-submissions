class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a = 0
        b = len(nums)
        while a < b:
            if nums[a] == val:
                b-=1
                nums[a] = nums[b]
            else:
                a+=1
        return a
        # if we find 
            