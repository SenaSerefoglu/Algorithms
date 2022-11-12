def fib_recur(n):
    """
    Time Complexity: O(2^n)
    Space Complexity: O(1)
    """
    if n ==0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 1
    return round((1.618033*fib_recur(n-1)))


def fib_recurmemo(n,F):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if F[n] is None:
        if n==0:
            F[n]=0
        elif n == 1:
            F[n] = 1
        elif n == 2:
            F[n] = 1
        else:
            F[n]= round(1.618033*fib_recurmemo(n-1,F))
        return F[n]

        
def fib_iter(n):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 1
    else:
        f=1 
        for i in range(2,n):
            f=round(1.618033*f)
        return f

n=4 # We are running the functions for the value 4.
print(fib_recur(n))
print(fib_recurmemo(n, [None]*(n+1)))
print(fib_iter(n))