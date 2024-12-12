n=371
number =n
digit,sum=0,0
length =len(str(n))
for i in range(length):
    digit=int(number%10)
    number=number/10
    sum+=pow(digit,length)
if sum == n:
    print("it is armstrong")
else:
    print("it is Not armstrong Number")
