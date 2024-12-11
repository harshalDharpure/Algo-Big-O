#Solution 2: T=O(n) , S=O(n)

ht={0: 0, 1: 1}
def fibonacci(n):
    if n in ht:
        return ht[n]
    else:
        ht[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return ht[n]  


print(fibonacci(4))
