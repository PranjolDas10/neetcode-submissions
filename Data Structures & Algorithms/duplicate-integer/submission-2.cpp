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

        for(auto num : nums) {
            if(seenSet.count(num)) {
                return true;
            }

            seenSet.insert(num);
        }
        return false;
    }
};