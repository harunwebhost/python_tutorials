# my_tuples = ('a',1,'2','2')
# #list1 = ['0','1','2']
# print (len(list1 ))

# def two_values (n1,n2):
#     return n1+n2,n1*n2,n1-n2

# add,multiple,substract = two_values(20,30)
# print("This is substraction",substract)
# print("This is addition",add)

list1 = [1,2,3,4,[1,2]]
total = 0
for i in list1:
    if type(i) == list:
        len(i)