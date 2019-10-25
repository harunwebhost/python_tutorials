# def cube_find(user_number):
#     cube_number = {}
#     for i in range(user_number):
#         cube_number[i] = i*i*i  
#     return cube_number
# print(cube_find(4))

# name,age,fevrate=raw_input("enter user input saprated by |").split("|")
# fevrate = fevrate.split(",")
# distion = {"name" : name, "age" : age , "fevrate_movies" : fevrate}
# for i in distion:
#     print (i + "=" ,distion[i])

setv = {1,2,3}
setv.add(55)
if setv.remove(88) == True:
    print(setv )