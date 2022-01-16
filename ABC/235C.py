n,q = map(int,input().split())
a = list(map(int,input().split()))
ans = [-1]*q
cnt = {}
for i in range(n):
    stra=str(a[i])
    if  stra in cnt:
        cnt[stra].append(i+1)
    else:
        cnt[stra]=[i+1]
for i in range(q):
    qi = input().split()
    iq2=int(qi[1])
    if  qi[0] in cnt:
        if len(cnt[qi[0]])>=iq2:
            ans[i]=cnt[qi[0]][iq2-1]
for i in range(q):
    print(ans[i])