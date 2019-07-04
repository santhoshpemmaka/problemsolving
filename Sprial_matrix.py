#code
def spriral_matrix(num,m,n):
    k=l=0
    while k<m and l<n:
        for i in range(l,n):
            print(num[k][i],end=" ")
            
        k = k+1
        
        for i in range(k,m):
            print(num[i][n-1],end=" ")
            
        n=n-1
        if k<m:
            for i in range(n-1,l-1,-1):
                print(num[m-1][i],end=" ")
            m = m-1
        if l<n:
            for i in range(m-1,k-1,-1):
                print(num[i][l],end=" ")
            l = l+1
    print()
            
num = int(input())
for i in range(num):
    m,n = map(int,input().split())
    l1 = []
    l = list(map(int,input().split()))
    for i in range(0,len(l),n):
        l1.append(l[i:i+n])
    spriral_matrix(l1,m,n)
