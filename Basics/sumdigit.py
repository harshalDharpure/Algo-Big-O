# n=123
# sum=0
# for i in str(n):
#     sum+=int(i)
# print(sum)

##Additional using the While Loop

# num = 123
# sum=0
# while num!=0:
#      a=int(num%10)
#      sum+=a
#      num=num/10
# print(sum)


##using the resursion

num,sum = 123,0

def findsum(num,sum):
    if num==0:
        return sum
    digit =int(num%10)
    sum+=digit
    return findsum(num/10,sum)

print(findsum(num,sum))