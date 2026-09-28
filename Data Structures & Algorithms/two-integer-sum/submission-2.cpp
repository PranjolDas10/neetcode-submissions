class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seenNumbers;

        for(int i = 0; i < nums.size(); i++) {
            int compliment = target - nums[i];
            if(seenNumbers.contains(compliment)) {
                return {seenNumbers[compliment], i};
            }
            seenNumbers[nums[i]] = i;
        }
        return {};
    }
};
