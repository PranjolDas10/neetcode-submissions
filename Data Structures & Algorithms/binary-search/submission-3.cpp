class Solution {
public:
    int search(vector<int>& nums, int target) {
        int min = 0;
        int max = nums.size() - 1;

        while(min <= max) {
            int middle = (min + max)/2;
            if(target == nums[middle]) {
                return middle;
            }
            else if(target < nums[middle]) {
                max = middle - 1;
            }
            else if (target > nums[middle]) {
                min = middle + 1;
            }
        }
        return -1;
    }
};
