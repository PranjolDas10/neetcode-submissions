class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sList = {}

        for letter in s:
            sList[letter] = sList.get(letter, 0) + 1

        tList = {}
        for letterr in t:
            tList[letterr] = tList.get(letterr, 0) + 1
        return sList == tList