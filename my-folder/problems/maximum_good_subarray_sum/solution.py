class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        hash = {}
        pre_sum = 0
        mini = int(-1e18)
        ans = mini
        
        for num in nums:
            st = set()
            st.add(k - num)
            st.add(num - k)
            st.add(num + k)
            
            # print(diff1, diff2, k, num)
            # print( st)
            
            for diff in st:
                if diff in hash and abs(num - diff) == k:
                    ans = max(ans, (pre_sum + num) - hash[diff])
                    
            for diff in st:
                if abs(num - diff) == k and (num not in hash or hash[num] > pre_sum):
                    hash[num] = pre_sum
                    
            pre_sum += num
                
        return 0 if ans == mini else ans
            