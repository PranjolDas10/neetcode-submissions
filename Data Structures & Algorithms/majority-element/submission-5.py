class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # take advantage of the fact that only one elem
        # will have freq > n/2
        freq = defaultdict(int) # handles new values nicely, adds it if missing and then tracks freq
        n = len(nums)
        for num in nums:
            freq[num] += 1
            if freq[num] > n/2:
                return num