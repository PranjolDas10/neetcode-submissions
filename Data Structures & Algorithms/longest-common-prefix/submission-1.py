class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])): # loop through first word chars
            for word in strs: # loop throgugh each word
                if i == len(word) or word[i] != strs[0][i]:
                    # if i of first word reaches length of other word 
                    # or the charcater of word and first word dont match
                    return word[:i]
        return strs[0]


