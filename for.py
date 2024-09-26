# for loop is used to iterate

# userName = "Saksham Gupta"
# for x in userName:
#     print(x)
    
    
# print number from 1 to 10 using loop
# in c++ : for(int i=0;i<11;i++)
# for i in range(1,11):
#     print(i)
    
    
# make table
# n = int(input("Enter the number : "))
# for a in range(1,11):
#     print(a*n)



#find even number btw 1 to 20

# for a in range(1,11):
#     if a% 2 == 0:
#         print(a)



# find the odd numbera
#  for y in range(1, 14, 3): # 3 is use as increment operator to skip 3 digit as you can you can put any numberhere 
#     print(y)


#WAp to print 1 3 7 13 15 for 
for i in range(1, 16, 2):
    if i==9 or i==5:
        continue # skip the current literation
    else:
        print(i)
