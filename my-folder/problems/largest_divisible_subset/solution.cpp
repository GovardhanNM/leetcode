class Solution {
public:
    vector <int> findAns(int index, vector<int>& nums, map <int, vector <int>>& mp, int& n) {
        if (mp.find(index) != mp.end())
            return mp[index];

        vector <int> temp;
        
        for (int i = index - 1; i >= 0; i--) {
            if (nums[index] % nums[i] == 0) {
                vector <int> temp1 = findAns(i, nums, mp, n);
                if (temp1.size() > temp.size())
                    temp = temp1;
            }
        }

        temp.push_back(nums[index]);
        mp[index] = temp;
        return temp;
    }

    vector<int> largestDivisibleSubset(vector<int>& nums) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        map <int, vector <int>> mp;

        vector <int> ans;
        for (int i = 0; i < n; i++) {
            vector <int> temp = findAns(i, nums, mp, n);
            // cout << temp.size() <<endl;
            if (temp.size() > ans.size())
                    ans = temp;
        }

        return ans;
    }
};