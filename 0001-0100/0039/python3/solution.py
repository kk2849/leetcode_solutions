from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        uniqueCombinations = []
        candidates.sort() # sort candidates
        #  candidates is max length of 30, values up to 200
        
        #dfs list for the current sum for each num in candidates
        def dfs_helper(current_list, current_sum):
            if current_sum == 0:
                uniqueCombinations.append(current_list)
            
            for num in candidates:
                #can't reach current_sum with bigger numbers, don't add duplicate combinations
                if num > current_sum or current_list and num < current_list[-1]:
                    continue
                else:
                    dfs_helper(current_list + [num], current_sum - num)
        
        dfs_helper([], target)
        return uniqueCombinations

    def main(self):
        print('case 1 - Input: candidates = [2,3,6,7], target = 7 Output: [[2,2,3],[7]]')
        if self.combinationSum([2,3,6,7], 7) == [[2,2,3],[7]]:
            print('case 1 passed')
        else:
            print('case 1 failed')

        print('case 2 - Input: candidates = [2,3,5], target = 8 Output: [[2,2,2,2],[2,3,3],[3,5]]')
        if self.combinationSum([2,3,5], 8) == [[2,2,2,2],[2,3,3],[3,5]]:
            print('case 2 passed')
        else:
            print('case 2 failed')

        print('case 3 - Input: candidates = [2], target = 1 Output: []')
        if self.combinationSum([2], 1) == []:
            print('case 3 passed')
        else:
            print('case 3 failed')

        print('case 4 - Input: candidates = [1], target = 1 Output: [[1]]')
        if self.combinationSum([1], 1) == [[1]]:
            print('case 4 passed')
        else:
            print('case 4 failed')

        print('case 5 - Input: candidates = [1], target = 2 Output: [[1,1]]')
        if self.combinationSum([1], 2) == [[1,1]]:
            print('case 5 passed')
        else:
            print('case 5 failed')

if __name__ == '__main__':
    Solution().main()