from typing import List

class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        tasks.sort()

        numSessions = 0

        tempSessionTime = sessionTime

        while tasks:
            while tempSessionTime != 0:
                last_idx = 1
                if tempSessionTime > tasks[-last_idx]:
                    tempSessionTime - tasks[-last_idx]
            

        return numSessions

    def main(self):
        print('case 1 - Input: tasks = [1,2,3], sessionTime = 3 Output: 2')
        if self.minSessions([1,2,3], 3) == 2:
            print('case 1 passed')
        else:
            print('case 1 failed')
            print(self.minSessions([1,2,3], 3))

        print('case 2 - Input: tasks = [3,1,3,1,1], sessionTime = 8 Output: 2')
        if self.minSessions([3,1,3,1,1], 8) == 2:
            print('case 2 passed')
        else:
            print('case 2 failed')
            print(self.minSessions([3,1,3,1,1], 8))

        print('case 3 - Input: tasks = [1,2,3,4,5], sessionTime = 15 Output: 1')
        if self.minSessions([1,2,3,4,5], 15) == 1:
            print('case 3 passed')
        else:
            print('case 3 failed')
            print(self.minSessions([1,2,3,4,5], 15))

        print('case 4 - Input: tasks = [8,8,8,8,8], sessionTime = 10 Output: 5')
        if self.minSessions([8,8,8,8], 10) == 5:
            print('case 4 passed')
        else:
            print('case 4 failed')
            print(self.minSessions([8,8,8,8], 10))

        print('case 5 - Input: tasks = [1,5,7,10,3,8,4,2,6,2], sessionTime = 10 Output: 5')
        if self.minSessions([1,5,7,10,3,8,4,2,6,2], 10) == 5:
            print('case 5 passed')
        else:
            print('case 5 failed')
            print(self.minSessions([8,8,8,8], 10))

if __name__ == '__main__':
    Solution().main()