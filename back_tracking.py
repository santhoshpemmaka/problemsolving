# Back tracking problem
# cook your dish here

def find(res,n,x,y,path):
    if x<0 or x>=n:
        return False
    
    if y<0 or y>=n:
        return False
        
    if x==n-1 and y==n-1:
        return True
        
    if res[x][y]==0 or path[x][y]==1:
        return False
        
    path[x][y]=1
    
    #Right
    if find(res,n,x,y+1,path):
        
        return True
        
    #Left
    if find(res,n,x,y-1,path):
        
        return True
        
    #Top
    if find(res,n,x-1,y,path):
    
        return True
        
    #Bottom
    if find(res,n,x+1,y,path):
    
        return True
        
    return False


def findpath(res,n):
    path = [[0]*(n) for i in range(n)]
    return find(res,n,0,0,path)

num = int(input())
res = []
for i in range(num):
    x = list(map(int,input().split()))
    res.append(x)
print(findpath(res,num))
"""
4
1 1 0 0
0 1 0 0
0 1 0 0
0 1 0 1
"""
