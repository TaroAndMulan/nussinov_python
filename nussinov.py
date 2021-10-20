import numpy as np
import sys

def nussinov_to_dot(sequence):

    def score(base_1,base_2):
        if (base_1 == "A"):
            return 1 if base_2=="U" else 0
        if (base_1 == "U"):
            return 1 if base_2=="A" or base_2=="G" else 0
        if (base_1 == "C"):
            return 1 if base_2=="G" else 0
        if (base_1 == "G"):
            return 1 if base_2=="C" or base_2=="U" else 0

    def generate_matrix(s):
        n = len(s)
        M = np.zeros((n,n))
        # iterate from 1st diagonal to last diagonal(upper right)
        for d in range(1,n):
            for i in range(n-d):
                j=i+d
                j_paired_k = max([M[i,k-1]+M[k+1,j-1]+score(s[k],s[j])\
                                for k in range(i,j)])
                j_unpaired = M[i,j-1]
                M[i,j] = max(j_paired_k,j_unpaired)
        return M
        
    def traceback(M,P,s,i,j):
        if j<=i:
            return 
        if M[i,j]==M[i,j-1]:
            traceback(M,P,s,i,j-1)
            return
        else:
            for k in range(i,j):
                if score(s[k],s[j])==1 and M[i,j]==(M[i,k-1]+M[k+1,j-1]+1):
                    P.append((k,j))
                    traceback(M,P,s,i,k-1)
                    traceback(M,P,s,k+1,j-1)
                    return

    def pairs_to_dot(pairs,length):
        dot = ["."]*length
        for p in pairs:
            dot[p[0]] = "("
            dot[p[1]] = ")"
        return "".join(dot)
            
    s = sequence
    M = generate_matrix(s)
    P=[]
    traceback(M,P,s,0,len(s)-1)
    return pairs_to_dot(P,len(s))

#print (nussinov_to_dot("GGGAAAUCC"))

print (nussinov_to_dot(sys.argv[1]))
     

