import time

num= input()
cnt=0
if int(num)<10:
    num = '0' + num

doing=''
while num!= doing:
    if doing=='':
        doing=num

    if len(str(int(doing[0])+int(doing[1])))>1:
        doing=doing[1]+str(int( doing[0])+int( doing[1]))[1]
        cnt+=1


    else:
        doing =  doing[1] + str(int( doing[0]) + int( doing[1]))
        cnt +=1

print(cnt)
