class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        counter = 0
        max_two_step = n/2
        for two_step in range(max_two_step+1):
            one_step = n-two_step*2
            combination = self.combination(two_step+one_step, one_step)
            counter+=combination
        return counter
            
            
    #combination m choose n
    def combination(self, m, n):
        def factorial(int_num):
            if int_num<0: return None
            if int_num==0: return 1
            counter = 1
            while int_num>=1:
                counter*=int_num
                int_num-=1
            return counter
        
        return factorial(m)/(factorial(n)*factorial(m-n))

#2020/11/9
class Solution(object):
    def climbStairs(self, n):
        def helper(n):
            if n in history: return history[n]
            
            if n==0 or n==1:
                history[n] = 1
            elif n==2:
                return 2
            elif n>2:
				#combination count of n stairs equals to
				#(the combination after you make 1 step as first move) + (the combination after you make 2 steps as first move)
                history[n] = helper(n-1) + helper(n-2)
            
            return history[n]
            
        history = {}
        return helper(n)        