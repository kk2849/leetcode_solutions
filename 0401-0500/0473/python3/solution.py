class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if not matchsticks:
            return False
        
        # so we can check biggest sticks first
        matchsticks.sort(reverse=True)
        
        array_sum = sum(matchsticks)
        
        # can't make a square
        if array_sum % 4 != 0:
            return False
        
        sq_len = array_sum / 4
        
        def dfs(sticks, stick_num, side):
            if stick_num == len(sticks): 
                return True
            for i in range(4): # check each of 4 sides
                if side[i] >= sticks[stick_num]:
                    side[i] -= sticks[stick_num]
                    if dfs(sticks, stick_num+1, side): 
                        return True
                    side[i] += sticks[stick_num]
            return False
        
        side = [sq_len] * 4 # same as [sq_len, sq_len, sq_len, sq_len]
        return dfs(matchsticks, 0, side)