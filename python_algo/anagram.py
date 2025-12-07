class Solution:
    def isAnagram(self,s: str,t: str) -> bool:
        # anagram , nagaram
        if len(s) != len(t):
            return False
        
        countS , countT = {},{}
        #s ={a:3,n:1,g:1,r:1,m:1...}
        #t ={n:1,a:3,g:1,r:1,m:1...}

        for i in range(len(s)):# 0 ,1,2,3,4,5,6 
            # Alternative using zip:
            # for s_char, t_char in zip(s, t):
            #     countS[s_char] = 1 + countS.get(s_char, 0)
            #     countT[t_char] = 1 + countT.get(t_char, 0) 
            countS[s[i]] =  1 + countS.get(s[i],0)
            countT[t[i]] =  1 + countT.get(t[i],0)  

        for c in countS: # a,n,r,m
            if countS[c] != countT.get(c,0):
                return False
        
        return True



s = Solution()
print(s.isAnagram("anagram", "nagaram"))





        
