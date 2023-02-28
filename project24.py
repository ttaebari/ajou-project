def crt(a,b,c,x,y,z):
    n1 = y*z 
    n2 = x*z 
    n3 = x*y
    for i in range(1,n1):
        if (n1*i) % x == 1 :
            u1 = i
            break
    for j in range(1,n2):
        if (n2*j) % y == 1 :
            u2 = j
            break
    for k in range(1,n3):
        if (n3*k) % z == 1 :
            u3 = k
            break
    D = a*n1*u1 + b*n2*u2 + c*n3*u3
    D = D%(x*y*z)
    return D
