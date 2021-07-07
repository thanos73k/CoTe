bool_list=[False]*30
ans=[]

for i in range(28):
    value=int(input())
    bool_list[value-1]=True

for i in range(30):
    if bool_list[i]==False:
        ans.append(i+1)

ans.sort()
print(ans[0])
print(ans[1])


