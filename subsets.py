def subsets(kume):
    if len(kume) == 0:
        return [[]]
    else:
        smaller = subsets(kume[1:])
        return smaller + [s + [kume[0]] for s in smaller]
    
print(subsets([1,2,3,4,5]))