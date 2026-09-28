class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        // Questions:
        // - can arrray be empty, if empty what -- return false
        // - size range?
        //brute force:
        // - start at first index and compare each one after that
        // - go to next index and do same
        // time complex is ON^2
        // optimized
        // nums.size()
        unordered_set<int> seenSet;

        for(int i = 0; i < nums.size(); i++) {
            int current = nums[i];

            if(seenSet.count(current)) {
                return true;
            }

            seenSet.insert(current);
        }
        return false;
    }
};