def pythonic_bs(l,key):

    if len (l) == 1:
        return l[0] == key
    if  l[len(l) // 2:][0] <= key:
        return pythonic_bs(l[len(l)//2:],key)
    else:
        return pythonic_bs(l[:len(l)//2],key)

def bs(l, x, low, high):

    if high-low == 1:
        return l[high] == x
    mid = (low+high)//2
    if l[mid] == x:
        return True
    if l[mid]>= x:
        return bs(l,x,low,mid)
    else:
        return bs(l,x,mid,high)
