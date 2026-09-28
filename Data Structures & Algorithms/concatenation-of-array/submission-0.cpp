class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> ans(nums.size() * 2);
        //int count = 0;
        for(int i = 0; i < nums.size(); i++) {
            ans[i] = nums[i];
            //count++;
        }
        for(int j = 0; j < nums.size(); j++) {
            ans[nums.size() + j] = nums[j];
        }
        return ans;
    }
};