class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int n = nums.size();
        vector<int>ans(n*2);

        for(int num; num<n; num++){
            ans[num] = nums[num];
            ans[num+n] = nums[num];
        }
        return ans;
    }
};