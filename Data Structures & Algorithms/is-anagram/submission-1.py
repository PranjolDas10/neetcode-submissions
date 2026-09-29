class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_freq1 = {}
        letter_freq2 = {}

        for char in s:
            if(char in letter_freq1):
                letter_freq1[char] = letter_freq1[char] + 1
            else:
                letter_freq1[char] = 0

        for char in t:
            if(char in letter_freq2):
                letter_freq2[char] = letter_freq2[char] + 1
            else:
                letter_freq2[char] = 0

        if letter_freq1 == letter_freq2:
            return True
        else:
            return False