class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // start with the first index and compare with the other indices number
        // if not found go to next index and do the same
        //Time complex ON^2
        unordered_map<int, int> seenMap;

        for(int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i]; //number we want to find

            if(seenMap.find(complement) != seenMap.end()) { //check if complement in map
                return {seenMap[complement], i}; //if so output the index compliment at and current
            }
            seenMap[nums[i]] = i; //add the current number to the array
        }
        return {};
    }
};
