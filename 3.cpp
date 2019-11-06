class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int start=0,end=1,max_l=1,sl=s.length(),l=1;
        if (sl==0) return 0;
        while ( end<sl )
        {
            string cur_s = s.substr(start,l);
            string::size_type idx = cur_s.find(s.substr(end,1));
            if ( idx != string::npos )
            {
                start += 1+idx;
                if ( start==end )
                {    
                    end = start+1;
                }
            }
            else
            {
                end++;
            }
            
            l = end-start;
            if (l>max_l) 
            {
                max_l = l;
            }
        }
        return max_l;
    }
};
