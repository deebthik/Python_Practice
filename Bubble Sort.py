L=list(input('enter a list'))
print 'Unsorted List :',L 
for i in range(len(L)-1):
    for j in range(len(L)-i-1): 
        if L[j]>L[j+1]:
            L[j],L[j+1]=L[j+1],L[j]
        
print 'Sorted List :',L