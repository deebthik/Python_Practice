def insertion_sort(l):
    for i in range (1, len(l)):
        temp=l[i] 
        ptr=i-1 
        while(ptr>=0) and l[ptr]>temp:
            l[ptr+1] = l[ptr] 
            ptr -= 1
            l[ptr+1] = temp

a=[5,2,6,1,4]
print "Before sort", a 
insertion_sort(a)
print "After sort ", a