class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a = 0 #slow pointer
        for i in range(len(nums)): # fast pointer
            if nums[i] != val: # only swap when a value found that != val
                nums[a] = nums[i] # else just keep iterating on adjacent vals
                a+=1 # will just swap with itself if adjacent !val which is safe
        return a