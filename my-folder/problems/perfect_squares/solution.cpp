class Solution {
public:
    int numSquares(int n) {
        vector <int> dp(n, 0);

        for (int i = 0; i < n; i++) {
            int num = i + 1;
            int root = sqrt(num);

            if (root * root == num) {
                dp[i] = 1;
                continue;
            }

            dp[i] = num;

            for (int j = 1; j <= 100; j++) {
                int rem = num - (j * j);
                if (rem > 0) {
                    dp[i] = min(dp[i], 1 + dp[rem - 1]);
                }
                else {
                    break;
                }
            }
        }  
        cout << endl;

        return dp[n - 1];
    }
};