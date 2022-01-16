a,n = map(int,input().split())
ans=0
bcnt=0

while a!=n:
    if a==n:
        print(ans)
        break
    elif n%a==0:
        n = n//a
        ans+=1
        bcnt=0
    elif n>10 and str(n)[-2]!="0" and bcnt < 7:
        ans+=1
        bcnt+=1
        strn=str(n)
        n=int(strn[1:]+strn[0])
    else:
        print(-1)
        break