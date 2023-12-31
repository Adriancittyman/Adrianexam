class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0 or strs==None:
            return ''
        
        bench_mark = strs[0] #[0]
        
        for i in range(1, len(bench_mark)+1): #[1]
            common_substring = bench_mark[:i]
            for s in strs:
                if s[:i]!=common_substring: #[2]
                    return bench_mark[:i-1]
        return bench_mark #[3]

# 2021/7/10
class Solution(object):
    def longestCommonPrefix(self, strs):
        j = 0
        minLen = float('inf')
        for s in strs: minLen = min(minLen, len(s))
        if minLen==float('inf'): return ""
        
        while j<minLen:
            c = strs[0][j]
            for i in xrange(1, len(strs)):
                if strs[i][j]!=c: return strs[i][:j]
            j += 1
            
        return strs[0][:j]        