#========================== Loops in python =====================================


#=========================practice question by using loops ================
 #Print numbers from 1 to 100. 
 
# n=1
# while n<=100 :
#     print(n)
#     n+=1



    #=======================second question========================
#Print numbers from 100 to 1. 
# n=100
# while n>=1 :
#         print(n)
#         n-=1
    
   
#=============================third question ==========================
#Print the multiplication table of a number n. 

# n=int(input("Enter your number you want to print the table of these number ="))
# i=1
# while i<=10 :
#     print(n,"*",i,"=",n*i)
#     i+=1



#===========the are use by infinate value will be print they have no limited======================

# n=int(input("Enter your number you want to print the table of these number ="))
# i=1
# while True :
#     print(n,"*",i,"=",n*i)
#     i+=1




#==============================four question ========================
#Print the elements of the following list using a loop: 
#[1, 4, 9, 16, 25, 36, 49, 64, 81,100] 

# num=[1, 4, 9, 16, 25, 36, 49, 64, 81,100] 
# print(len(num))
# i=0
# while i<len(num ):
#     print(num[i])
#     i+=1



#================================= For loops in python ===========================
# lis=[1,3,4,5,6,4,]
# for vale in lis :
#     print(vale)


#==================================practic question using for loop===============
# Print the elements of the following list using a loop: 
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100] 

# list=[1, 4, 9, 16, 25, 36, 49, 64, 81,100] 
# for val in list :
#     print(val)




    #===============================second question for loop============
#Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100] 
# vales=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# x=49
# index =4
# for i in vales :
#     if(i==x) :
#         print("value found in index =", index)
#     index += 1






    #===============================lets practics question using range in for loop===================
# Print numbers from 1 to 100. 
# for i in range(1,101,1) :
#     print(i)




    #====================================second question ===================
    #Print numbers from 100 to 1.
    # sit=range(100,0,-1)
    # for j in sit :
    #     print(j)
    

    #=====================================third question ===============
    #Print the multiplication table of a number n. 
n=int(input("enter your number ="))
for a in range(1,11,2) :
        print(n * a)
        