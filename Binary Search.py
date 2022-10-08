L=list(input('enter a list')) 
x=input('enter the search value') 
beg=0
end=len(L)
pos=-1
while beg<=end:
    mid=(beg+end)/2 
    if x==L[mid]:
        pos=mid
        break 
    elif x>L[mid]:
        beg=mid
    else:
        end=mid
    
            
if pos==-1:
    print 'Element not found or not a sorted list' 
else:
    print 'The value is present in location ',pos + 1