def A(n):
    if n != 0:
        return n * A(n-1)
    else:
        return 1


print(A(5))