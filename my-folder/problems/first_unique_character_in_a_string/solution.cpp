class Solution {
public:
    int firstUniqChar(string s) {
        vector <int> count(26);
        vector <int> first(26, -1);

        for (int i = 0; i < s.size(); i++) {
            char ch = s[i];
            if (first[ch - 'a'] == -1) {
                first[ch - 'a'] = i;
            }

            count[ch - 'a']++;
        }

        int ans = INT_MAX;
        for (int i = 0; i < 26; i++) {
            if (count[i] == 1) {
                ans = min(ans, first[i]);
            }
        }

        return ans == INT_MAX ? -1 : ans;
    }
};