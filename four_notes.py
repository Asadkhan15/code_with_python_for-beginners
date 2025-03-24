# #============================Dictionary and set in python=======================

# dic={
#     "rollno" : 1,
#     "name" : "Asad khan",
#     "subject" : ["python","java","c++","javascript"],
#     "address" : "regi aftezai peshawar"
# }

# print(dic)
# print(type(dic))

# print(dic["address"])
# dic["city"]="peshawar"
# print(dic)


# #============================Nested Dictionary======================================

# student = {
#     "name":"asad khan",
#      "subject" : ["python","java","c++",],
#     "marks" :{
#         "python ": 98,
#         "java" : 99,
#         "c++": 97
#     }
# }

# print(student)
# print(type(student))

# print(student["marks"]["java"])

# #===========================Dictionary Method========================================

# print(student.keys()) #they are print all key in student dictionary

# print(student.items()) #they are print all key and value in student dictionary

# print(student.values())  #they are print all value in student dictionary

# print(student.get("name"))   #return the key according to their values

# print(student.update({"country" : "pakistan"})) #the will update the value in dictionary

# new_dic ={
#     "gpa" :"3.4"
# }

# print(student.update(new_dic))
# print(student)



#====================================Set in python==================================

collection={1,2,3,"asad khan","peshawar"}
print(len(collection))

#=================================set method in python===========================

asad=set()  #if you create a empty set so you will use these syntax
# print(asad)
asad.add(1)   # if you add some value and empty set so you will use these syntax
asad.add(2)
asad.add("asad")
asad.remove(1)   # if you remove value these syntax
print(asad)

asad.clear()
print(len(asad))  #if you clear your set so use these


#==========================================union and intersection in set in python=================================

student1={1,2,3,5,4}     #union in set 
student2={1,3,5,8,9,6}
print(student1.union(student2))

student3={2,1,5,7,5,2}   #intersection in set
student4={5,9,8,1,7,}
print(student3.intersection(student4))





#===============================Practice question of python===============

# Store following word meanings in a python dictionary : 
# table : “a piece of furniture”, “list of facts & figures”
#  cat : “a small animal”

dic={
    "table ": ["a piece of furniture" ,"list of facts and figures"],
    "cat" : "a small animal"
}
print(dic)




#===============================second question===============
#  You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
#  ”python”, “java”, “C++”, “python”, “javascript”,
#  “java”, “python”, “java”, “C++”, “C”

students={
    "python","java","c++","python","javascript","java","python","java","c++","c"
}
print(students)
print(len(students))




# ===================================third question====================================
# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
#  an empty dictionary & add one by one. Use subject name as key & marks as value.

subject1="python"
subject2="java"
subject3="javascript"

marks1 =input("enter your python marks =")
marks2 =input("enter your java marks =")
marks3 =input("enter your javascript marks =")

dictionary = {}
dictionary.update({"python":marks1})
dictionary.update({"java":marks2})
dictionary.update({"javascript":marks3})
print(dictionary)




#===================================four question=================
# Figure out a way to store 9 & 9.0 as separate values in the set. 
#(You can take help of built-in data types) 

value=(9, "9.0")
print(value)

values={"int": 9,
        "float" : 9.0   }
print(values)