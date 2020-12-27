def is_even(p):
    n= len(p)
    count= 0 # count == number of transposition used so far
    s= 0 # s minimal elements are at their places 0..s-1
    while s != n:
        # fill p[s] correctly by finding min p[s..n-1]:
        i= s
        t= s+1
        # when t<=n, p[i] is minimal among p[s]..p[t-1]
        while t != n:
            if p[t]<p[i]:
                i= t
            t+= 1
        # t==n, p[i] is minimal among p[s]..p[n-1]
        p[s],p[i]=p[i],p[s]; count+= 1
        s+= 1
    return count%2==0

print(is_even([2,0,1]))
