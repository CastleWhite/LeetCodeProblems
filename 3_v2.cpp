class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int start=0,max_l=1,sl=s.length(),l;
        if (sl==0) return 0;
        unordered_set<char> set;
        for (int i=0;i<sl;i++)
        {
            while (set.find(s[i]) != set.end())
            {
                set.erase(s[start++]);
            }
            set.insert(s[i]);
            l = i-start+1;
            max_l = (max_l<l) ? l:max_l;
        }
        return max_l;
    }
};
