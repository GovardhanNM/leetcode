class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string prefix = strs[0];
        int end = prefix.size();

        for (int i = 1; i < strs.size(); i++) {
            end = min(end, (int)strs[i].size());
            for (int j = 0; j < end; j++) {
                if (strs[i][j] != prefix[j]) {
                    end = j;
                    break;
                }
            }
        }

        return prefix.substr(0, end);
    }
};