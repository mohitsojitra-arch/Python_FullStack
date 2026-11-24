# Rearrange array such that A[A[i]] is set i for every element A[i]
# Input:{1, 3, 4, 2, 0}
# Output:{4, 0, 3, 1, 2}
# Explanation:
# A[0] = 1, A[1] becomes 0
# A[1] = 3, A[3] becomes 1
# A[2] = 4, A[4] becomes 2
# A[3] = 2, A[2] becomes 3
# A[4] = 0, A[0] becomes 4



list1=[1,3,4,2,0]
ans=[0]*len(list1)

print(list1)

for i in range(0,len(list1),1):
    ans[list1[i]]=i

print(ans)