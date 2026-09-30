class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #loop through until the letter is not the same across all
        # keep the first word in a variable then 

        first_word = strs[0]

        for i, char in enumerate(first_word): #will loop through each char of the first word
            for s in strs[1:]: #go through the 2nd,3rd... all letters in each one/one
                if i == len(s) or char != s[i]:
                    return first_word[:i]
        return first_word