base , labo , price = map(int, input().split())

if price-labo ==0:
    print(-1)
    quit()

sol =(base//(price-labo))+1
if sol <0:
    print(-1)
else:
    print(sol)

