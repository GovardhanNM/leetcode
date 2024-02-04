class Solution {
public:
    void addCharacter(int index, string& s, map <char, int>& count, map <char, int>& hash, int& currLength) {
        char ch = s[index];
        count[ch]++;
        if (hash.find(ch) == hash.end())
            return;

        if (hash[ch] >= count[ch])
            currLength++;
    }

    void deleteCharacter(int index, string& s, map <char, int>& count, map <char, int>& hash, int& currLength) {
        char ch = s[index];
        count[ch]--;
        if (hash.find(ch) == hash.end())
            return;

        // cout << hash[ch] << " " << count[ch] << endl;
        if (hash[ch] > count[ch])
            currLength--;
    }

    string minWindow(string s, string t) {
        int n = s.size();
        int m = t.size();
        map <char, int> hash;
        map <char, int> count;

        for (auto &ch: t) 
            hash[ch]++;

        int end = 0;
        int start = 0;
        int currLength = 0;
        int minStart = -1;
        int minEnd = -1;
        int minLength = INT_MAX;
        string ans = "";

        while (end < n) {
            while (end < n && currLength < m) {
                addCharacter(end++, s, count, hash, currLength);
            }

            if (currLength == m) {
                // cout << start << " " << end << endl;
                if (minLength > (end - start)) {
                    minLength = (end - start);
                    minStart = start;
                    minEnd = end - 1;
                }
            }

            while (start < end && (currLength >= m || hash.find(s[start]) == hash.end())) {
                deleteCharacter(start++, s, count, hash, currLength);
                if (currLength == m) {
                    // cout << start << " " << end << endl;
                    if (minLength > (end - start)) {
                        minLength = (end - start);
                        minStart = start;
                        minEnd = end - 1;
                    }
                }

                // cout << start << " " << currLength << endl;
            }
            // cout << end << " " << start << " " << currLength << endl;
        }

        if (minLength != INT_MAX) {
            ans = s.substr(minStart, minLength);
        }

        return ans;

    }
};