number = input("Enter the no. : ")
number_string = str(number)
sum = 0
sum2 = 0

for i in number_string:
    sum += int(i)
    
while(len(str(sum)) > 1):
        for i in str(sum):
            sum2 += int(i)
        sum = sum2
        sum2 = 0
        
print sum

if(sum == 1):
    print "It is a magic number !"
else:
    print "It is not a magic number"


    
    