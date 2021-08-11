class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int l = nums.size();
        vector<vector<int>> res;
        for (int i = 0; i < l-3; i ++){
            if (i && nums[i] == nums[i-1]) continue;
            int a = nums[i];
            for (int j = i+1; j < l-2; j ++){
                if (j > i+1 && nums[j] == nums[j-1]) continue;
                int b = nums[j];
                int x = j+1, y = l-1, nt = target - a - b;
                while (x < y){
                    int c = nums[x], d = nums[y];
                    if (c + d == nt){
                        vector<int> t {a, b, c, d};
                        res.push_back(t);
                        while (++ x < y && nums[x] == c);
                        while (x < -- y && nums[y] == d);
                    }
                    else if (c + d < nt){
                        while (++ x < y && nums[x] == c);
                    }
                    else while (x < -- y && nums[y] == d);
                }
            }
        }
        return res;
    }
};
