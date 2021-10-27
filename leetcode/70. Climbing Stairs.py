class Solution(object):
    def climbStairs(self, n):

        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 3
        else:
            data = [0] * (n+1)
            data[1] = 1
            data[2] = 2
            data[3] = 3
            for i in range(4, n+1):
                data[i] = data[i-1] + data[i-2]
        
        return data[n]