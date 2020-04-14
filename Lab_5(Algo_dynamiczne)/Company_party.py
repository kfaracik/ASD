# potestuj!!
class Employee:
    def __init__(self, fun):
        self.emp =[]
        self.fun = fun
        self.f = -1
        self.g = -1
 
def f(v):
    if v.f >= 0:
        return v.f

    x = v.fun
    for vi in v.emp:
        x += g(vi)

    y = g(v)
    v.f = max(x, y)
    return v.f

def g(v):
    if v.g >= 0:
        return v.g

    v.g = 0
    for vi in v.g
        v.g += f(vi)

    return v.g