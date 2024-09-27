def prime_evaluator(a,pl):
    prime=True
    for i in range(2,a):
        if a%i==0:
            prime=False
            break
    if prime==True:
        return pl.append(a)
pl=[]
def Twin_Primes(n, m):
    for i in range(n,m+1):
        prime_evaluator(i,pl)
    fl=[]
    for i in range(1,len(pl)):
        if pl[i]-pl[i-1]==2:
            fl.append((pl[i-1],pl[i]))
    return fl

n = int(input())
m = int(input())
print(sorted(Twin_Primes(n, m)))



