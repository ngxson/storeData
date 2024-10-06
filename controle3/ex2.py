

def ed(L,M=[]):
    if not(L):
        return M
    a = L.pop(0)
    if a not in M:
        M.append(a)
    return ed(L,M)

def ed_iterative(L):
    M=[]
    for a in L:
        if a not in M:
            M.append(a)
    return M

L = [2,3,2,6,8,9,9,10,9,3,6,7,8,8,9]
print(ed(L))
L = [2,3,2,6,8,9,9,10,9,3,6,7,8,8,9]
print(ed_iterative(L))
