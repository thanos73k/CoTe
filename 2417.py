num= int(input())

start =0
end = num

while start <= end:
    mid = (start + end)//2

    if mid **2 < num:
        start = mid +1

    else:
        end = mid-1

print(start)