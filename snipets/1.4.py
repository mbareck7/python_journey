#nsmallest & nlargest items in a list

def nsmallest(l,n):
    l.sort()
    return l[:n]

def nlargest(l,n):
    l.sort(reverse=True)
    return l[:n]

if __name__ == '__main__':
    numbers = [3,2,1,6,2,3,6,-94,10,232]
    print(nsmallest(numbers,3),"nsmallest")
    print(nlargest(numbers,3),"nlargest")