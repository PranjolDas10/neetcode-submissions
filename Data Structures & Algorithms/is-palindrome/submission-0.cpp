class Solution {
public:
    bool isPalindrome(string s) {
        int first = 0; //first index
        int last = s.length() - 1; //last index
        //come inwards and check the values are the same
        while(first < last) {
            if (!isalnum(s[first])) {
                first++;
                continue;
            }
            if (!isalnum(s[last])) {
                last--;
                continue;
            }
            char a = tolower(s[first]);
            char b = tolower(s[last]);
            if(a != b) {
                return false;
            }
            first++;
            last--;
        }
        return true;
    }
};
