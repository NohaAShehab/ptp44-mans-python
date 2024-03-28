# # if (name ==='ahmed'){
# #
# # console.log("Hello world")
# # }
# name = 'ahmed'
#
#    # name2 = 'ali'
# # if name=='ahmed':
# #     print("hello world")
#
# bio = "My name is Noha"\
#        "I lives in cairo"
#
# bio = ("My name is Noha"
#        "I lives in cairo")
#
#
# bio= """My name is Noha
# I works at ITI
# I lives in Mansoura"""
#
# print(bio)
#
#
#
# """ this is considered to be a comment """
#
#
# age= 31
#
# # fname = 'noha'
# # midname = 'Abdelhady'
# # lname=  'shehab'
#
# # fullname = f"{fname} {lname} {midname}"
#
#
# ### loop over the string
#
# # name ="                               "
# # print(name.isspace())
#
#
# #################33 list
#
# l = []
# myl = list()
#
#
# myl = [34,4, "iti", 344.32, "ahmed", True, ['kubernates', 'GCP', "ansible"], "iti"]
#
#
# # print("iti"> "python")
# #
# # print("iti"> 10)
# #
# # lst_of_courses = []
# # lst_of_courses.sort()
#
#
# t = ()
# myt = tuple()
#
#
#
# students = ("Ahmed Nagy",)  # tuple of one item
# print(students, type(students))
#
#
#
# #########################
#
#
#
# """
#        construct list of number from 1 to 10
#
# """
#
# num = 0
# numberss= []
# while num < 10:
#        numberss.append(num)
#        num = num + 1
# print(numberss) # 000--> 9

### datatype ranges ---> based on sequence

myr = range( 10 )    # return range object ---> start 0 ,, step 1 ,, stop  10
print(myr)

"cast to a list"
# items = list(myr)
# print(items)
#
# for num in myr:
#        print(num)

# myr = range(1, 10 ,2)
# print(list(myr))

# myss = set()
# mys = {"Ahmed", "Zeinab", "iti", 3234, "Ahmed", "Mohamed", "Mohamed","Mohamed", 3.12}
#
# print(mys)
# print(len(mys))



### dict


# info = ["noha", "iti", 31, "mansoura", "python"]
# # unlabeled data ---> reperesent data in terms of key:value



d = {} # dict
myd = dict()

info ={'name': 'Noha Shehab',
       'age': 32, 'track': 'OSAD', 'courses': ['python', 'bash', 'linux']}
print(info)

keys = info.keys()
keys_list = list(info)
print(keys_list)



print(info.items())  # dict_itmes
ll = list(info.items())



"""
       noha ---> 2 ---> 
       
       
       itinoha iti iti  ---> 3
       
       
       noha ----> nh
       
       
       3 ---> 
       
       [
              [1],   # 1*1 
              [2,4],
              [3,6,9]
       ]
       
"""



## NERVER TRUST USER INPUT ===>
# YOU must validate --> input ==> can be converted to string or not






















