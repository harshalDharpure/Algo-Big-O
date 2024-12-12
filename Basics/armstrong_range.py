low,high = 10,10000
for i in range(low,high+1):
    order=len(str(i))
    sum=0
    temp=i
    while temp>0:
        digit =int(temp%10)
        sum+=digit ** order
        temp=temp/10
        
    if i==sum:
        print(i,end=',')