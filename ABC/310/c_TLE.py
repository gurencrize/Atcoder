ls = []
ans = 0
def search(s:str,n:int):
    idx = ls.index(s)
    idx_min = 0
    try:
        idx_r = ls.index(s[::-1])
        idx_min = min(idx,idx_r)
    except:
        idx_min = idx
    if idx_min == n:
        return True
    else:
        return False

n = int(input())
for i in range(n):
    ls.append(input())
for i in range(n):
    if search(ls[i],i):
        ans += 1
print(ans)