def reached(st):
    m=0
    n=len(st)
    for i in range(n):
        if i>m:
            return False
        m=max(m, i+st[i])
        if m>= n-1:
            return True
    return False
st=eval(input())
print(reached(st))
