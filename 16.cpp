class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int l = nums.size();
        // for (auto num: nums)
        int s = 100000;
        for (int i = 0; i < l-2; i ++){
            int a = nums[i];
            int nt = target - a;
            int left = i+1, right = l-1;
            while (left < right){
                if (nums[left] + nums[right] == nt) return target;
                else if (nums[left] + nums[right] < nt){
                    if (nt - nums[left] - nums[right] < abs(s)) s = nt - nums[left] - nums[right];
                    left ++;
                } 
                else{
                    if (nums[left] + nums[right] - nt < abs(s)) s = nt - nums[left] - nums[right];
                    right --;
                } 
            }
        }
        return target - s;
    }
};
