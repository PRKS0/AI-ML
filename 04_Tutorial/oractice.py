def f1(p1):
    def f2(p2):
        return p2 ** p1
    return f2

v1 = f1(2)
v2 = v1(3)
print(9)