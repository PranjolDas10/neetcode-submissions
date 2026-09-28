class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length() != t.length()) {
            return false;
        }

        unordered_map<char,int> letterS;
        unordered_map<char,int> letterT;

        for(int i = 0; i < s.length(); i++) {
            letterS[s[i]]++;
            letterT[t[i]]++;
        }
        return letterS == letterT;
    }
};
