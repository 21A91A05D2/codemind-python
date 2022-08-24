class Solution:
    def previousNumber (ob,S):
        
        S=list(S)
        idx1=-1
        for i in range(len(S)-1,0,-1):
            if S[i]<S[i-1]:
                idx1=i-1
                break
            
        if idx1==-1:
            return -1
        
        mx=S[idx1+1]
        idx2=idx1+1
        for i in range(idx1+1,len(S)):
            if S[i]>mx and S[i]<S[idx1]:
                mx=S[i]
                idx2=i
                
        S[idx2],S[idx1]=S[idx1],S[idx2]
        
        if S[0]=='0':
            return -1
        
        return ''.join(S)
        
        
S = str (input ())

ob = Solution()
print(ob.previousNumber(S))
