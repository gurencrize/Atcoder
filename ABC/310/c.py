ans = set()
n = int(input())
for i in range(n):
    s = input()
    ans.add(min(s,s[::-1]))
print(len(ans))