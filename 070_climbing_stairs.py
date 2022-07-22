"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top?
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        return int( (((1+5**0.5)/2)**(n+1) - ((1-5**0.5)/2)**(n+1)) / 5**0.5 )
