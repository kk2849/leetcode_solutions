#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> sol;
        for (int i=0; i<nums.size(); ++i) {
            for(int j=i+1; j<nums.size(); ++j){
                    int daSum = nums[i]+nums[j];
                    if (daSum == target) {
                        sol.push_back(i);
                        sol.push_back(j);
                    }
            }
        }   
        return sol;
    }
};