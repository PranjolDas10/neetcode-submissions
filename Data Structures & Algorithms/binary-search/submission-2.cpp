class Solution {
public:
    int search(vector<int>& nums, int target) {
        int low = 0;
        int max = nums.size() - 1;

        while(low <= max) {
            int middle = (low+max) / 2;
            if(target == nums[middle]) {
                return middle;
            }
            else if(target < nums[middle]) {
                max = middle -1;
            }
            else if(target > nums[middle]) {
                low = middle + 1;
            }
        }
        return -1;
    }
};
