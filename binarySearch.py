def binary_search(ls,element):
    l = len(ls)
    left=0
    right= l-1
    while left<=right:
        mid = (left+right)//2
        if ls[mid]==element:
            return mid
        elif ls[mid]<element:
            left=mid+1
        else:
            right=mid-1
    return -1
if __name__=="__main__":
    ls,element = list(map(int,input().split())), int(input())
    ls.sort()
    print("sorted sequence:",ls)
    print("index:",binary_search(ls,element))
    
