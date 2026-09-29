class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        letter_freq1, letter_freq2 = {}, {}

        for i in range(len(t)): #since the length is the same
            letter_freq1[s[i]] = 1 + letter_freq1.get(s[i], 0) # the 0 is the check if there or not
            letter_freq2[t[i]] = 1 + letter_freq2.get(t[i], 0)

        return letter_freq1 == letter_freq2
