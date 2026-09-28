class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> ans;;
        //int count = 0;
        for(int i = 0; i < 2; i++) {
            for(int num : nums) {
                ans.push_back(num);
            }
        }
        return ans;
    }
};