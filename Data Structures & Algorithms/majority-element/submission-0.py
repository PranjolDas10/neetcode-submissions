class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # track freq of elements -> hashmap
        freq = {}

        for val in nums:
            freq[val] = freq.get(val, 0) + 1 #.get, 0 for default case
        return max(freq, key=freq.get)
            