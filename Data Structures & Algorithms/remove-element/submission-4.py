class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a = 0
        for i in range(len(nums)):
            if(nums[i] != val):
                nums[a] = nums[i]
                a+=1
        return a
        # a is slow point and i is fast
        # if nums[i] not val. then jus swap with itself at beginning
        # if i is val, a will alr be there and i will continue until !val
            #then swap the val with nonval
        