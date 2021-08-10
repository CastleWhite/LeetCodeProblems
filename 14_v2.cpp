class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.size() == 1) return strs[0];
        sort(strs.begin(), strs.end());
        string r = strs[0];
        int res = r.size();
        for (int i = 1; i < strs.size(); i ++){
            for (int j = 0; j < res; j ++){
                if (r[j] != strs[i][j]){
                    res = j;
                    break;
                }
            }
            if (res == 0) return "";
        }
        return r.substr(0, res);
    }
};
