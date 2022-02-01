"""GCD of two numbers using euclidean algorithm"""

"""Euclidean algorithm

1.the GCD does of two numbers does not change,even if we subract the smallest number from the largest one
2.so we do this recursively untill we find the GC
pro tip...repeated subraction is division..thus use modulo operator to find if the other number is divisible by the other"""

# this is a recursive function----terminates only when b==0 or becomes invalid
def gcd(a,b):
    # checking if b=0
    if b==0:
        return a
    # if not 0,then b is the greater on enow,because for sure a%b will be less than a
    # remember we wrote def gcd assuming a is always greater
    return gcd(b,a%b)

# driver code:
a=int(input("a"))
b=int(input("b"))

# find the greatest among the two,since the def is written considering a is the greater than b
if b>a:
    b,a=a,b
    
# if the does return anything then it changes to TRUE.thus if condition becomes TRUE.
# If true print the ans,else print 1, because the given 2 numbers are not having any divisor in common other than 1
ans=gcd(a,b)
if ans:
    print(ans)
else:
    print("1")
